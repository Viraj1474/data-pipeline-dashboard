# Employee Data Pipeline

A simple Python-based ETL (Extract, Transform, Load) pipeline for processing employee data. This project demonstrates the core concepts of data extraction, cleaning, transformation, and storage.

## Overview

The data pipeline processes raw employee data through several stages:

1. **Extract** - Reads raw employee CSV data from the source
2. **Transform** - Cleans data, handles missing values, and creates new calculated fields
3. **Load** - Saves the processed data to the output directory

The pipeline is designed to be simple and easy to understand while following standard data engineering practices.

## Project Structure

```
data_pipeline/
├── data/
│   ├── raw/
│   │   └── employees.csv           # Raw input data
│   └── processed/
│       └── employees_processed.csv # Transformed output data
├── src/
│   ├── config.py                   # Configuration settings
│   ├── extract.py                  # Data extraction module
│   ├── transform.py                # Data transformation logic
│   ├── load.py                     # Data loading module
│   └── etl_run.py                  # Main pipeline orchestration
├── scripts/
│   └── generate_data.py            # Sample data generation script
├── dashboard/
│   └── streamlit_app.py            # Analytics dashboard
├── infra/
│   ├── Dockerfile                  # Container configuration
│   └── docker-compose.yml          # Multi-container setup
└── requirements.txt                # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone or download the project:
```bash
cd data_pipeline
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Generating Sample Data

Before running the pipeline, generate sample employee data:

```bash
python scripts/generate_data.py
```

This creates a CSV file with 200 randomly generated employee records in `data/raw/employees.csv`.

### Running the ETL Pipeline

Execute the complete pipeline:

```bash
python src/etl_run.py
```

This will:
- Extract data from the raw CSV file
- Transform and clean the data
- Save processed data to `data/processed/employees_processed.csv`

### Individual Pipeline Steps

You can also run each pipeline step independently:

**Extract:**
```bash
python src/extract.py
```

**Transform:**
```bash
python src/transform.py
```

**Load:**
```bash
python src/load.py
```

## Data Transformation Details

The transformation process includes:

- **Duplicate Removal** - Removes duplicate employee records based on ID
- **Missing Value Handling** - Fills missing age and salary values with the median
- **Department Standardization** - Replaces missing departments with "Unknown"
- **Calculated Fields**:
  - `tax` - 10% of salary
  - `net_salary` - Salary minus tax
  - `age_group` - Categorizes employees into Young (18-25), Mid (26-35), Senior (36-50), Veteran (51+)

## Configuration

Pipeline settings can be modified in [src/config.py](src/config.py):

- Data file paths
- Salary ranges for data generation
- Tax calculation rate
- Age group definitions

## Running with Docker

Build and run the pipeline using Docker:

```bash
cd infra
docker-compose up
```

## Dashboard

A Streamlit dashboard is available for data visualization and exploration:

```bash
streamlit run dashboard/streamlit_app.py
```

## Dependencies

Main libraries used:
- `pandas` - Data manipulation and analysis
- `faker` - Sample data generation
- `streamlit` - Dashboard framework

See [requirements.txt](requirements.txt) for the complete list of dependencies.

## Contributing

This is a learning project. Feel free to extend it with additional transformations, data validations, or new modules.

## Notes

- Raw data files should be placed in `data/raw/`
- Processed data is automatically saved to `data/processed/`
- The pipeline handles missing values by using median imputation for numeric fields
- All configurations are centralized in the config module for easy adjustments

## License

This project is open source and available for personal and educational use.
