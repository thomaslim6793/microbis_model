[![DOI](https://zenodo.org/badge/974597213.svg)](https://doi.org/10.5281/zenodo.15300235)

# Overview

This repository contains the backend code for  
**MicroBIS - An integrated AI laboratory Assistant for Bacteria and Antimicrobial Resistance Identification**.

The MicroBIS system is designed to assist laboratory professionals by providing AI-powered bacterial species identification and antimicrobial resistance (AMR) classification based on biochemical and genomic laboratory data.

---

# 🛠️ Repository Structure

The codebase is organized into two main components:

### 1. Model Training (`src/` folder)
- Contains scripts for training machine learning models:
  - Bacterial Identification Models
  - Antimicrobial Resistance (AMR) Classifier Models
- Uses **XGBoost** with GPU acceleration and **RandomizedSearchCV** for hyperparameter optimization.
- Saves trained models and evaluation metrics in local storage.

### 2. API Deployment (`app/` folder)
- Implements a **FastAPI** server to:
  - Load the trained models.
  - Provide API endpoints for real-time bacterial and AMR prediction.
  - Allow easy integration with external web or laboratory information systems.

---

# 📂 Dataset Requirement

The dataset required for training is available on Zenodo:

- **DOI**: [10.5281/zenodo.15300029](https://doi.org/10.5281/zenodo.15300029)

### Setup Instructions:

1. Download the `dataset.zip` file from the Zenodo archive.
2. Extract the contents of `dataset.zip`.
3. Place the extracted files into a new folder named `local_data/` at the root of this repository.

Example folder structure:

---

# ⚡ How to Train Models

To train the models manually, run the following commands:

```bash
cd src/
python train_gene_bin_classifier.py
python train_gene_mult_classifier.py
```

---

# License

This project is licensed under the [MIT License](LICENSE).

---

# Citation

If you use this code or dataset, please cite:

> Lim HS, Kwakye A, Huh CY, and Akligoh H. *MicroBIS - An integrated AI laboratory Assistant for Bacteria and Antimicrobial Resistance Identification.* 2025. DOI: [10.5281/zenodo.15300029](https://doi.org/10.5281/zenodo.15300029)
