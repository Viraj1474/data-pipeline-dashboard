import os

# Data paths
RAW_DATA_DIR = os.path.join("data", "raw")
PROCESSED_DATA_DIR = os.path.join("data", "processed")
RAW_DATA_PATH = os.path.join(RAW_DATA_DIR, "employees.csv")
PROCESSED_DATA_PATH = os.path.join(PROCESSED_DATA_DIR, "employees_processed.csv")

# Data generation settings
DEFAULT_SAMPLE_SIZE = 200
SALARY_MIN = 30000
SALARY_MAX = 100000
AGE_MIN = 18
AGE_MAX = 60

# Available departments
DEPARTMENTS = ["HR", "IT", "Finance", "Marketing"]

# Age group definitions
AGE_BINS = [0, 25, 35, 50, 100]
AGE_LABELS = ["Young", "Mid", "Senior", "Veteran"]

# Tax calculation
TAX_RATE = 0.1
