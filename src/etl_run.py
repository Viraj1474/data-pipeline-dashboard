from extract import extract
from transform import transform
from load import load

def run_etl():
    print("Starting ETL pipeline...")
    df_raw = extract()
    df_transformed = transform(df_raw)
    load(df_transformed)
    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_etl()
