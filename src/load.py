import pandas as pd
import os

PROCESSED_PATH = os.path.join("data", "processed", "employees_processed.csv")

def load(df: pd.DataFrame):
    """Save transformed data to processed folder"""
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Data successfully saved to {PROCESSED_PATH}.")

# Test independently
if __name__ == "__main__":
    from transform import transform
    from extract import extract
    
    df_raw = extract()
    df_transformed = transform(df_raw)
    load(df_transformed)
