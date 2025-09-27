# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Default command to run ETL and then Streamlit
CMD ["sh", "-c", "python src/etl_run.py && streamlit run dashboard/streamlit_app.py --server.port 8501 --server.address 0.0.0.0"]
