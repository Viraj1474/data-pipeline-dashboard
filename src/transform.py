import pandas as pd
import os

RAW_DATA_PATH = os.path.join("data", "raw", "employees.csv")

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="id")
    df['age'] = df['age'].fillna(df['age'].median())
    df['salary'] = df['salary'].fillna(df['salary'].median())
    df['department'] = df['department'].fillna("Unknown")
    df['tax'] = df['salary'] * 0.1
    df['net_salary'] = df['salary'] - df['tax']
    bins = [0, 25, 35, 50, 100]
    labels = ["Young","Mid","Senior","Veteran"]
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
    print(f"✅ Transformed data: {len(df)} rows")
    return df

if __name__ == "__main__":
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(f"{RAW_DATA_PATH} not found. Run generate_data.py first.")
    
    df = pd.read_csv(RAW_DATA_PATH)
    df2 = transform(df)
    print(df2.head())
