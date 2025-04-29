from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from joblib import load
import pickle
from typing import List, Dict
import pandas as pd
import json
import os
from dotenv import load_dotenv

class PredictionRequest(BaseModel):
    requested_model: str  # Changed from model_name to requested_model
    data: List[Dict]  # JSON array with dictionaries as input

    class Config:
        protected_namespaces = ()  # Optionally disable protected namespace warnings if needed

class PredictionResponse(BaseModel):
    predictions: List[str]

# Load models using joblib
bacterial_identification_models = {
    "rf_8_panel_enterobac_100": load('./models/rf_8_panel_enterobac_100.pkl'),
    "rf_20_panel_enterobac_100": load('./models/rf_20_panel_enterobac_100.pkl'),
}

# Load models using pickle with proper file handling
mic_and_gene_models = {}

with open('./models/mic_classification_best.pkl', 'rb') as file:
    mic_and_gene_models["mic_classification_best"] = pickle.load(file)

with open('./models/mic_i_classification_best.pkl', 'rb') as file:
    mic_and_gene_models["mic_i_classification_best"] = pickle.load(file)

with open('./models/gene_bin_classification_best.pkl', 'rb') as file:
    mic_and_gene_models["gene_bin_classification_best"] = pickle.load(file)

with open('./models/gene_mult_classification_best.pkl', 'rb') as file:
    mic_and_gene_models["gene_mult_classification_best"] = pickle.load(file)

# Unique categories for each column in the training set
def load_categories_for_model(model_name):
    json_file_path = f'./category_features_unique_values/{model_name}.json'
    with open(json_file_path, 'r') as file:
        categories = json.load(file)
    return categories

#### APP ####
# Load environment variables
load_dotenv()

app = FastAPI()

# Access the FRONTEND_URL environment variable and allow multiple origins
frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:5173')
origins = [
    frontend_url,            # The frontend URL from .env
    "http://52.14.24.164:5001",  # Your MERN app's URL in EC2
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Use the list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict", response_model=PredictionResponse)
def make_prediction(request: PredictionRequest):
    model_name = request.requested_model  # Adjusted to use requested_model
    print("model_name is: ", model_name)
    
    if model_name not in bacterial_identification_models and model_name not in mic_and_gene_models:
        raise HTTPException(status_code=404, detail=f"Model {model_name} not found.")
    
    try:
        # Convert the JSON data to a DataFrame
        input_data = pd.DataFrame(request.data)

        if model_name in bacterial_identification_models:
            predictions = bacterial_identification_models[model_name].predict(input_data) 
            predictions_as_strings = [str(pred) for pred in predictions]
            return PredictionResponse(predictions=predictions_as_strings)
        
        elif model_name in mic_and_gene_models:
            # Load category information for the model
            categories = load_categories_for_model(model_name)
            # Ensure that each column in input_data has the correct categories
            for col, cats in categories.items():
                input_data[col] = pd.Categorical(input_data[col], categories=cats)
            predictions = mic_and_gene_models[model_name]['model'].predict(input_data)            
            predictions_decoded = mic_and_gene_models[model_name]['label_encoder'].inverse_transform(predictions)     
            predictions_as_strings = [str(pred) for pred in predictions_decoded]
            return PredictionResponse(predictions=predictions_as_strings)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# New route to get category information for a model
@app.get("/categories/{model_name}")
def get_categories(model_name: str):
    try:
        categories = load_categories_for_model(model_name)
        return categories
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Multi-Model Prediction API"}
