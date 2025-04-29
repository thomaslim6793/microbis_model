import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump

# Load data
data_path = Path('../../pybact_data/enterobac_100_train_data.txt')
df = pd.read_csv(data_path, sep='\t')
df.rename({'Unnamed: 48': 'Target'}, axis=1, inplace=True)

# Load panel features
def load_panel(file_path):
    with open(file_path, 'r') as f:
        return [line.split(',', 1)[1].strip() for line in f]

columns_8 = load_panel('./panels/panels_8.txt')
columns_20 = load_panel('./panels/panels_20.txt')

# Train and save model function
def train_and_save_model(X, y, model_path):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Accuracy: {accuracy:.4f}")
    dump(model, model_path)

# 8-panel model
X_8 = df[columns_8]
y = df['Target']
models_dir = Path(__file__).resolve().parent.parent / 'models'
models_dir.mkdir(parents=True, exist_ok=True)
train_and_save_model(
    X=X_8, 
    y=y, 
    model_path=models_dir / 'rf_8_panel_enterobac_100.pkl'
)
# 20-panel model
X_20 = df[list(set(columns_20).intersection(df.columns))]
train_and_save_model(
    X=X_20, 
    y=y, 
    model_path=models_dir / 'rf_20_panel_enterobac_100.pkl'
)
