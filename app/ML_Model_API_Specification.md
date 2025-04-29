# ML Model API Specification

This document provides a detailed specification for the Machine Learning Model API. 
It outlines the available endpoints, input and output formats, and the expected data types for interacting with the API. 
This guide is intended for developers who need to integrate the machine learning models into their applications.

## Endpoints Overview

The API exposes the following endpoints:

- **`POST /predict`**: Takes in input data for a specified machine learning model and returns the prediction results.
- **`GET /`**: A simple endpoint to verify that the API is running, returning a welcome message.


### GET /

This endpoint is used to verify that the API is running correctly. It returns a simple welcome message.

- **URL**: `/`
- **Method**: `GET`

#### Example Response
```json
{
  "message": "Welcome to the Multi-Model Prediction API"
}
```

### POST /predict

This endpoint allows you to make predictions using one of the available machine learning models. You must specify the model name and provide the required input data in JSON format.

- **URL**: `/predict`
- **Method**: `POST`
- **Content-Type**: `application/json`

#### Request Format

The request must include the following fields:

- **`model_name`**: (string) The name of the machine learning model to use for predictions.
- **`data`**: (array of dictionaries) The input data for the model, where each dictionary represents a set of features for a single prediction.

#### Example Request
```json
{
  "requested_model": "rf_8_panel_enterobac_100",
  "data": [
    {
      "Urea_hydrolysis": 0, 
      "Lactose_fermentation": 1, 
      "D-Glucose_acid": 1,
      "Citrate": 0,
      "Motility": 0,
      "Indole_production": 0,
      "Hydrogen_Sulfide_TSI": 1,
      "D-Glucose_Gas": 1
    }
  ]
}
```

#### Response Format

The response will contain the prediction results as an array of strings.

- **`predictions`**: (array of strings) Each string corresponds to the predicted label for the input data.

#### Example Response
```json
{
  "predictions": ["C.gillenii"]
}
```

#### Error Handling

If the specified model is not found, or if there is an error with the input data, the API will return an error message.

```json
{
  "detail": "Model 'invalid_model_name' not found."
}
```

## **Model Specifications**
Details about the input features expected by the models.

### Input Feature Specifications

**`rf_8_panel_enterobac_100`** model:

- **`Urea_hydrolysis`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Lactose_fermentation`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`D-Glucose_acid`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Citrate`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Motility`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Indole_production`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Hydrogen_Sulfide_TSI`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`D-Glucose_Gas`**: 
  - Type: Integer
  - Range of values: {0, 1}

```json
{
  "requested_model": "rf_8_panel_enterobac_100",
  "data": [
    {
      "Urea_hydrolysis": 0, 
      "Lactose_fermentation": 1, 
      "D-Glucose_acid": 1,
      "Citrate": 0,
      "Motility": 0,
      "Indole_production": 0,
      "Hydrogen_Sulfide_TSI": 1,
      "D-Glucose_Gas": 1
    }
  ]
}
```

**`rf_20_panel_enterobac_100`** model:

- **`Indole_production`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`myo-Inositol_fermentation`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Gelatin_hydrolysis_22_c`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`D-Sorbitol_fermentation`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Arginine_dihydrolase`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`L-Rhamnose_fermentation`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Melibiose_fermentation`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Citrate`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Phenylalanine_deaminase`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Ornithine_decarboxylase`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`D-Glucose_acid`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Lysine_deaminase`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Urea_hydrolysis`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Voges-Proskauer`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Hydrogen_Sulfide_TSI`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`Sucrose_fermentation`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`D-Mannose_fermentation`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`ONPG_test`**: 
  - Type: Integer
  - Range of values: {0, 1}
- **`L-Arabinose_fermentation`**: 
  - Type: Integer
  - Range of values: {0, 1}

```json
{
  "requested_model": "rf_20_panel_enterobac_100",
  "data": [
    {
      "Indole_production": 0, 
      "myo-Inositol_fermentation": 1, 
      "Gelatin_hydrolysis_22_c": 1,
      "D-Sorbitol_fermentation": 0,
      "Arginine_dihydrolase": 1,
      "L-Rhamnose_fermentation": 0,
      "Melibiose_fermentation": 1,
      "Citrate": 0,
      "Phenylanine_deaminase": 1,
      "Ornithine_decarboxylase": 0,
      "D-Glucose_acid": 1,
      "Lysine_deaminase": 0,
      "Urea_hydrolysis": 1,
      "Voges-Proskauer": 0,
      "Hydrogen_Sulfide_TSI": 1,
      "Sucrose_fermentation": 0,
      "D-Mannose_fermentation": 1,
      "ONPG_test": 0,
      "L-Arabinose_fermentation": 1
    }
  ]
}
```

**`mic_i_classification_best`** model:

- **`Phenotype`**: 
  - Type: Category
- **`Species`**: 
  - Type: Category
- **`Family`**: 
  - Type: Category
- **`Country`**: 
  - Type: Category
- **`State`**: 
  - Type: Category
- **`Gender`**: 
  - Type: Category
- **`Age Group`**: 
  - Type: Category
- **`Speciality`**: 
  - Type: Category
- **`Source`**: 
  - Type: Category
- **`In / Out Patient`**: 
  - Type: Category
- **`Year`**: 
  - Type: Integer
- **`Antibiotic`**: 
  - Type: Category

```json
{
  "requested_model": "mic_i_classification_best",
  "data": [
    {
      "Phenotype": "MRSA",
      "Species": "Staphylococcus aureus",
      "Family": "Staphylococcus spp",
      "Country": "Australia",
      "State": null,  
      "Gender": "Male",
      "Age Group": "85 and Over",
      "Speciality": "Medicine General",
      "Source": "Sputum",
      "In / Out Patient": "Inpatient",
      "Year": 2013,
      "Antibiotic": "Erythromycin"
    }
  ]
}

{
  "requested_model": "mic_i_classification_best",
    "data": [
        {
        "Phenotype": null,
        "Species": "Pseudomonas aeruginosa",
        "Family": "Non-Enterobacterales",
        "Country": "Brazil",
        "State": null,
        "Gender": "Female",
        "Age Group": "19 to 64 Years",
        "Speciality": "Medicine ICU",
        "Source": "Peritoneal Fluid",
        "In / Out Patient": null,
        "Year": 2022,
        "Antibiotic": "Ceftazidime avibactam"
    }
  ]
}
```

**`mic_classification_best`** model:

- **`Phenotype`**: 
  - Type: Category
- **`Species`**: 
  - Type: Category
- **`Family`**: 
  - Type: Category
- **`Country`**: 
  - Type: Category
- **`State`**: 
  - Type: Category
- **`Gender`**: 
  - Type: Category
- **`Age Group`**: 
  - Type: Category
- **`Speciality`**: 
  - Type: Category
- **`Source`**: 
  - Type: Category
- **`In / Out Patient`**: 
  - Type: Category
- **`Year`**: 
  - Type: Integer
- **`Antibiotic`**: 
  - Type: Category

```json
{
  "requested_model": "mic_classification_best",
  "data": [
    {
      "Phenotype": null,
      "Species": "Pseudomonas aeruginosa",
      "Family": "Non-Enterobacterales",
      "Country": "China",
      "State": null,
      "Gender": "Male",
      "Age Group": "19 to 64 Years",
      "Speciality": "Surgery ICU",
      "Source": "Blood",
      "In / Out Patient": null,
      "Year": 2022,
      "Antibiotic": "Amikacin"
    }
  ]
}

{
  "requested_model": "mic_classification_best",
  "data": [
    {
      "Phenotype": "MSSA",
      "Species": "Staphylococcus aureus",
      "Family": "Staphylococcus spp",
      "Country": "Finland",
      "State": null,
      "Gender": "Male",
      "Age Group": "19 to 64 Years",
      "Speciality": "None Given",
      "Source": "Nose",
      "In / Out Patient": "None Given",
      "Year": 2006,
      "Antibiotic": "Ampicillin"
    }
  ]
}
```

**`gene_bin_classification_best`** model:

- **`Phenotype`**: 
  - Type: Category
- **`Species`**: 
  - Type: Category
- **`Family`**: 
  - Type: Category
- **`Country`**: 
  - Type: Category
- **`State`**: 
  - Type: Category
- **`Gender`**: 
  - Type: Category
- **`Age Group`**: 
  - Type: Category
- **`Speciality`**: 
  - Type: Category
- **`Source`**: 
  - Type: Category
- **`In / Out Patient`**: 
  - Type: Category
- **`Year`**: 
  - Type: Integer
- **`gene`**: 
  - Type: Category

```json
{
  "requested_model": "`gene_bin_classification_best`",
  "data": [
    {
      "Phenotype": null,
      "Species": "Pseudomonas aeruginosa",
      "Family": "Non-Enterobacteriaceae",
      "Country": "Spain",
      "State": null,
      "Gender": "Female",
      "Age Group": "65 to 84 Years",
      "Speciality": "Medicine General",
      "Source": "Sputum",
      "In / Out Patient": null,
      "Year": 2018,
      "gene": "KPC"
    }
  ]
}

{
  "requested_model": "gene_bin_classification_best",
  "data": [
    {
      "Phenotype": "ESBL",
      "Species": "Klebsiella pneumoniae",
      "Family": "Enterobacteriaceae",
      "Country": "South Africa",
      "State": null,
      "Gender": "Male",
      "Age Group": "19 to 64 Years",
      "Speciality": "Medicine General",
      "Source": "Wound",
      "In / Out Patient": "Inpatient",
      "Year": 2016,
      "gene": "TEM"
    }
  ]
}
```

**`gene_mult_classification_best`** model:

- **`Phenotype`**: 
  - Type: Category
- **`Species`**: 
  - Type: Category
- **`Family`**: 
  - Type: Category
- **`Country`**: 
  - Type: Category
- **`State`**: 
  - Type: Category
- **`Gender`**: 
  - Type: Category
- **`Age Group`**: 
  - Type: Category
- **`Speciality`**: 
  - Type: Category
- **`Source`**: 
  - Type: Category
- **`In / Out Patient`**: 
  - Type: Category
- **`Year`**: 
  - Type: Integer
- **`gene`**: 
  - Type: Category

```json
{
  "requested_model": "gene_mult_classification_best",
  "data": [
    {
      "Phenotype": "ESBL",
      "Species": "Escherichia coli",
      "Family": "Enterobacteriaceae",
      "Country": "Kuwait",
      "State": null,
      "Gender": "Female",
      "Age Group": "19 to 64 Years",
      "Speciality": "Medicine General",
      "Source": "Skin: Other",
      "In / Out Patient": "Inpatient",
      "Year": 2016,
      "gene": "CTXM1"
    }
  ]
}

{
  "requested_model": "gene_mult_classification_best",
  "data": [
    {
      "Phenotype": "ESBL",
      "Species": "Klebsiella pneumoniae",
      "Family": "Enterobacteriaceae",
      "Country": "Portugal",
      "State": null,
      "Gender": "Male",
      "Age Group": "65 to 84 Years",
      "Speciality": "Medicine ICU",
      "Source": "Sputum",
      "In / Out Patient": "Inpatient",
      "Year": 2012,
      "gene": "TEM"
  }
  ]
}
```

### Output Feature Specifications

**`rf_8_panel_enterobac_100`** model:
  - Type: Category
  
**`rf_20_panel_enterobac_100`** model:
  - Type: Category

**`mic_i_classification_best`** model:
  - Type: Category

**`mic_classification_best`** model:
  - Type: Category

**`gene_bin_classification_best`** model:
  - Type: Category
  
**`gene_mult_classification_best`** model:
  - Type: Category

### 6. **Final Notes**
End with any additional notes or considerations.

```markdown
### Additional Notes

- Ensure that the input data is formatted correctly according to the specified feature requirements.
- The API is designed to handle multiple models, so ensure the correct `model_name` is provided in the request.
- For any issues or questions, please contact the API developer.