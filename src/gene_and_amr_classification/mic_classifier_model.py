from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV
import json
import pickle
from pathlib import Path

local_data_path = Path(__file__).resolve().parent.parent.parent / 'local_data'

df = pd.read_csv(local_data_path / 'amr_data_long_format_no_genes.csv',
                 dtype={'MIC': 'str', 'MIC_Interpretation': 'str'})

# Define df_MIC by dropping 'MIC_Interpretation' column
df_MIC = df.drop(columns=['MIC_Interpretation'])

# Drop all rows where 'MIC' is NaN
df_MIC = df_MIC.dropna(subset=['MIC'])

# Define the target variable (y) and the feature set (X)
y = df_MIC['MIC']
X = df_MIC.drop(columns=['MIC'])

# Convert categorical columns to 'category' dtype
categorical_columns = ['Phenotype', 'Species', 'Family', 'Country', 'State', 
                       'Gender', 'Age Group', 'Speciality', 'Source', 'In / Out Patient', 'Antibiotic']

for col in categorical_columns:
    if col in X.columns:
        X[col] = X[col].astype('category')

# Convert any numeric columns to the appropriate type if necessary
numeric_columns = X.select_dtypes(include=['int64', 'float64']).columns

# Optionally convert other numeric-like columns that might be object types
for col in numeric_columns:
    X[col] = pd.to_numeric(X[col], errors='coerce')

# Identify classes with only one instance
class_counts = y.value_counts()
rare_classes = class_counts[class_counts == 1].index

# Filter out the rows with these rare classes
X = X[~y.isin(rare_classes)]
y = y[~y.isin(rare_classes)]

# Encode the target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded)


# Define the parameter grid for hyperparameter tuning
param_dist = {
    'max_depth': [3, 4, 5, 6, 7, 8, 9, 10],
    'learning_rate': [0.01, 0.05, 0.1, 0.2, 0.3],
    'n_estimators': [50, 100, 200, 300],
    'subsample': [0.6, 0.7, 0.8, 0.9, 1.0],
    'colsample_bytree': [0.6, 0.7, 0.8, 0.9, 1.0],
    'gamma': [0, 0.1, 0.2, 0.3, 0.4],
    'min_child_weight': [1, 3, 5, 7]
}

# Initialize the XGBClassifier with default parameters
model = xgb.XGBClassifier(
    tree_method='gpu_hist',  # Use the GPU-accelerated histogram algorithm
    gpu_id=0,  # Use the first GPU
    eval_metric='mlogloss',  # Evaluation metric
    use_label_encoder=False,  # To avoid deprecation warnings
    enable_categorical=True  # Enable native handling of categorical features
)

# Perform RandomizedSearchCV with cross-validation
random_search = RandomizedSearchCV(
    model, 
    param_distributions=param_dist, 
    n_iter=15,  # Number of different combinations to try
    scoring='accuracy',  # Metric to optimize
    cv=4,  # 5-fold cross-validation
    verbose=1,  # Print progress
    n_jobs=-1  # Use all available cores
)

# Fit the RandomizedSearchCV object to find the best model
random_search.fit(X_train, y_train)

# Get the best model from the search
best_model = random_search.best_estimator_

# Evaluate the best model on the test set
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Best model test set accuracy: {accuracy}")

# Combine the best model and label encoder into a dictionary
model_and_encoder = {
    'model': best_model,
    'label_encoder': label_encoder
}

# Save the combined object to a pkl file
with open(local_data_path / 'mic_classification_best.pkl', 'wb') as file:
    pickle.dump(model_and_encoder, file)

print("Best model and label encoder saved as 'mic_classification_best.pkl'")

# Calculate metrics after training
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_, output_dict=True)
conf_matrix = confusion_matrix(y_test, y_pred)

# Save the metrics
metrics = {
    'accuracy': accuracy,
    'classification_report': report,
    'confusion_matrix': conf_matrix.tolist()  # Convert to list for JSON serialization
}

with open(local_data_path / 'mic_classification_metrics.json', 'w') as file:
    json.dump(metrics, file)

print("Model metrics saved as 'mic_classification_metrics.json'")


