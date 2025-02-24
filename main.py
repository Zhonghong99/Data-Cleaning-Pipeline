import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import ydata_profiling
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class DataCleaningPipeline:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        logging.info("Loading data...")
        file_ext = os.path.splitext(self.file_path)[1].lower()

        if file_ext == ".csv":
            self.data = pd.read_csv(self.file_path)
        elif file_ext == ".xlsx":
            self.data = pd.read_excel(self.file_path, engine='openpyxl')
        elif file_ext == ".json":
            self.data = pd.read_json(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please use .csv, .xlsx, or .json")
        
        logging.info(f"Data loaded successfully with shape {self.data.shape}.")

    def generate_eda_report(self, output_path="eda_report.html"):
        logging.info("Generating EDA report...")
        report = ydata_profiling.ProfileReport(self.data)
        report.to_file(output_path)
        logging.info(f"EDA report saved to {output_path}.")

    def encode_categorical_columns(self):
        """Encode categorical columns before imputation"""
        logging.info("Encoding categorical columns...")
        for col in self.data.select_dtypes(include=["object"]).columns:
            if col == "sex":  # Encode sex column specifically
                self.data[col] = self.data[col].map({"male": 1, "female": 0})
            # Add more categorical encodings here if needed
            # elif col == "another_categorical_column":
            #     self.data[col] = self.data[col].map({"value1": 1, "value2": 2})

    def handle_missing_values(self, strategy="mean"):
        logging.info("Handling missing values...")
        # First encode categorical variables
        self.encode_categorical_columns()
        
        # Handle numeric columns
        numeric_cols = self.data.select_dtypes(include=["float64", "int64"]).columns
        if len(numeric_cols) > 0:
            num_imputer = SimpleImputer(strategy=strategy)
            self.data[numeric_cols] = num_imputer.fit_transform(self.data[numeric_cols])
        
        # Handle any remaining categorical columns with mode imputation
        categorical_cols = self.data.select_dtypes(include=["object"]).columns
        if len(categorical_cols) > 0:
            cat_imputer = SimpleImputer(strategy="most_frequent")
            self.data[categorical_cols] = cat_imputer.fit_transform(self.data[categorical_cols])

    def remove_duplicates(self):
        logging.info("Removing duplicates...")
        before = len(self.data)
        self.data.drop_duplicates(inplace=True)
        after = len(self.data)
        logging.info(f"Removed {before - after} duplicate rows.")

    def clean_text_columns(self):
        logging.info("Cleaning text columns...")
        for col in self.data.select_dtypes(include=["object"]).columns:
            self.data[col] = self.data[col].str.strip().str.lower()

    def standardize_data(self):
        logging.info("Standardizing numerical columns...")
        scaler = StandardScaler()
        num_cols = self.data.select_dtypes(include=["float64", "int64"]).columns
        self.data[num_cols] = scaler.fit_transform(self.data[num_cols])

    def export_cleaned_data(self, output_path="cleaned_data.csv"):
        logging.info(f"Exporting cleaned data to {output_path}...")
        self.data.to_csv(output_path, index=False)
        logging.info("Data exported successfully.")

# Example usage
if __name__ == "__main__":
    pipeline = DataCleaningPipeline("E:\DOCUMENTS\Open Online Class\Data Science Analyst\Own projectss\data_cleaning_pipeline\insurances_dataset.csv")
    pipeline.load_data()
    pipeline.generate_eda_report(output_path=r"E:\DOCUMENTS\Open Online Class\Data Science Analyst\Own projectss\data_cleaning_pipeline\eda_report.html")
    pipeline.handle_missing_values()
    pipeline.remove_duplicates()
    pipeline.clean_text_columns()
    pipeline.standardize_data()
    pipeline.export_cleaned_data(output_path=r"E:\DOCUMENTS\Open Online Class\Data Science Analyst\Own projectss\data_cleaning_pipeline\cleaned_data.csv")
