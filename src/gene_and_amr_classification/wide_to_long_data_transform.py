import pandas as pd
from pathlib import Path

# Define the list of antibiotics and their corresponding interpretation columns
antibiotics = [
    'Amikacin', 'Amoxycillin clavulanate', 'Ampicillin', 'Azithromycin', 'Cefepime', 'Cefoxitin', 'Ceftazidime',
    'Ceftriaxone', 'Clarithromycin', 'Clindamycin', 'Erythromycin', 'Imipenem', 'Levofloxacin', 'Linezolid',
    'Meropenem', 'Metronidazole', 'Minocycline', 'Penicillin', 'Piperacillin tazobactam', 'Tigecycline',
    'Vancomycin', 'Ampicillin sulbactam', 'Aztreonam', 'Aztreonam avibactam', 'Cefixime', 'Ceftaroline',
    'Ceftaroline avibactam', 'Ceftazidime avibactam', 'Ciprofloxacin', 'Colistin', 'Daptomycin', 'Doripenem',
    'Ertapenem', 'Gatifloxacin', 'Gentamicin', 'Moxifloxacin', 'Oxacillin', 'Quinupristin dalfopristin',
    'Sulbactam', 'Teicoplanin', 'Tetracycline', 'Trimethoprim sulfa', 'Ceftolozane tazobactam', 'Cefoperazone sulbactam',
    'Meropenem vaborbactam', 'Cefpodoxime', 'Ceftibuten', 'Ceftibuten avibactam', 'Tebipenem'
]

antibiotics_interpretations = [
    'Amikacin_I', 'Amoxycillin clavulanate_I', 'Ampicillin_I', 'Azithromycin_I', 'Cefepime_I', 'Cefoxitin_I',
    'Ceftazidime_I', 'Ceftriaxone_I', 'Clarithromycin_I', 'Clindamycin_I', 'Erythromycin_I', 'Imipenem_I',
    'Levofloxacin_I', 'Linezolid_I', 'Meropenem_I', 'Metronidazole_I', 'Minocycline_I', 'Penicillin_I',
    'Piperacillin tazobactam_I', 'Tigecycline_I', 'Vancomycin_I', 'Ampicillin sulbactam_I', 'Aztreonam_I',
    'Aztreonam avibactam_I', 'Cefixime_I', 'Ceftaroline_I', 'Ceftaroline avibactam_I', 'Ceftazidime avibactam_I',
    'Ciprofloxacin_I', 'Colistin_I', 'Daptomycin_I', 'Doripenem_I', 'Ertapenem_I', 'Gatifloxacin_I', 'Gentamicin_I',
    'Moxifloxacin_I', 'Oxacillin_I', 'Quinupristin dalfopristin_I', 'Sulbactam_I', 'Teicoplanin_I', 'Tetracycline_I',
    'Trimethoprim sulfa_I', 'Ceftolozane tazobactam_I', 'Cefoperazone sulbactam_I', 'Meropenem vaborbactam_I',
    'Cefpodoxime_I', 'Ceftibuten_I', 'Ceftibuten avibactam_I', 'Tebipenem_I'
]

genes = ['AMPC', 'SHV', 'TEM', 'CTXM1', 'CTXM2', 'CTXM825', 'CTXM9', 'VEB',
       'PER', 'GES', 'ACC', 'CMY1MOX', 'CMY11', 'DHA', 'FOX', 'ACTMIR', 'KPC',
       'OXA', 'NDM', 'IMP', 'VIM', 'SPM', 'GIM']

# Define other column groups
isolate_id = ['Isolate Id']
phenotype = ['Phenotype']
isolate_features = ['Species', 'Family']
meta_and_patient_features = ['Country', 'State', 'Gender', 'Age Group', 'Speciality', 'Source', 'In / Out Patient', 'Year']


def transform_to_long_format(input_file, output_file, antibiotics, antibiotics_interpretations, isolate_id, phenotype, isolate_features, meta_and_patient_features):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Initialize lists to store the long format data
    long_format_data = []

    # Iterate over the antibiotics and their corresponding interpretation columns
    for antibiotic, interpretation in zip(antibiotics, antibiotics_interpretations):
        temp_df = df[isolate_id + phenotype + isolate_features + meta_and_patient_features].copy()  # Exclude genes columns
        temp_df['Antibiotic'] = antibiotic
        temp_df['MIC'] = df[antibiotic]
        temp_df['MIC_Interpretation'] = df[interpretation]
        long_format_data.append(temp_df)

    # Concatenate all the dataframes into one
    df_long = pd.concat(long_format_data, axis=0, ignore_index=True)

    # Save the transformed DataFrame to a CSV file
    df_long.to_csv(output_file, index=False)

    print(f"Transformed dataset saved to {output_file}")

def transform_to_long_format_gene_target(input_file, output_file, genes, 
                                         isolate_id, phenotype, isolate_features, 
                                         meta_and_patient_features):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Initialize a list to store the long format data
    long_format_data = []

    # Iterate over the genes
    for gene in genes:
        temp_df = df[isolate_id + phenotype + isolate_features + meta_and_patient_features].copy()  # Exclude genes columns
        temp_df['gene'] = gene
        temp_df['detected_variant'] = df[gene]
        long_format_data.append(temp_df)

    # Concatenate all the dataframes into one
    df_long = pd.concat(long_format_data, axis=0, ignore_index=True)

    # Save the transformed DataFrame to a CSV file
    df_long.to_csv(output_file, index=False)

    print(f"Transformed dataset saved to {output_file}")


# Specify input and output file paths

local_data_path = Path(__file__).resolve().parent.parent.parent / 'local_data'
input_file = local_data_path / '2024_05_28 atlas_antibiotics.csv' 
output_file = local_data_path / 'amr_data_long_format_no_genes.csv'

# Transform the dataset
transform_to_long_format(input_file, output_file, antibiotics, 
                         antibiotics_interpretations, isolate_id, 
                         phenotype, isolate_features, meta_and_patient_features)
# Example usage
output_file = local_data_path / 'amr_data_long_format_no_antibiotics.csv'
transform_to_long_format_gene_target(input_file, output_file, 
                                     genes, isolate_id, phenotype, 
                                     isolate_features, meta_and_patient_features)
