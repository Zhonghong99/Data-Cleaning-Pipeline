# Data Cleaning Pipeline

This project provides a streamlined **data cleaning pipeline** using Python and **pandas**, designed to handle common data preprocessing tasks like handling missing values, encoding categorical data, removing duplicates, and standardization.

## Features

- 📂 **Load data**: Supports `.csv`, `.xlsx`, and `.json` formats.
- 🔍 **EDA Report**: Generates an Exploratory Data Analysis (EDA) report using `ydata_profiling`.
- 🔄 **Handle missing values**: Uses mean/mode imputation for numerical and categorical features.
- 🏷 **Encode categorical columns**: Supports mapping categorical variables like "sex" to numerical values.
- 📏 **Standardize numerical data**: Scales numerical features using `StandardScaler`.
- ✨ **Remove duplicates**: Identifies and removes duplicate rows.
- 📝 **Clean text columns**: Trims whitespace and converts text to lowercase.
- 💾 **Export cleaned data**: Saves the final dataset to a `.csv` file.

## Installation

Ensure you have Python 3.x installed. Then, install the required dependencies:
```bash
pip install pandas numpy scikit-learn ydata-profiling openpyxl

## Installation

1. Clone this repository
2. Install the required packages
## Requirements
- python
- pandas
- numpy
- scikit-learn
- ydata-profiling
- openpyxl

Modify `main.py` with the path to your dataset and run the script:

```bash
python main.py
```

### Example

```python
pipeline = DataCleaningPipeline("data.csv")  # Replace with your dataset
pipeline.load_data()
pipeline.generate_eda_report(output_path="eda_report.html")
pipeline.handle_missing_values()
pipeline.remove_duplicates()
pipeline.clean_text_columns()
pipeline.standardize_data()
pipeline.export_cleaned_data(output_path="cleaned_data.csv")
```

## File Structure
```
📂 Project Folder
│-- main.py               # Main script
│-- requirements.txt      # List of dependencies
│-- README.md             # Documentation
│-- data/                 # (Optional) Raw dataset folder
│-- output/               # (Optional) Processed output folder
```

## License
This project is licensed under the MIT License.
