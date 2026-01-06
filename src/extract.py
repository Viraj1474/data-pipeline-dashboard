import pandas as pd
import os

RAW_DATA_PATH = os.path.join("data", "raw", "employees.csv")

def extract():
    """Reads raw CSV data into a pandas DataFrame"""
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(f"{RAW_DATA_PATH} not found. Run scripts/generate_data.py first.")
    
    print(f"Extracting data from {RAW_DATA_PATH}...")
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"Successfully extracted {len(df)} rows.")
    return df

if __name__ == "__main__":
    df = extract()
    print(df.head())
