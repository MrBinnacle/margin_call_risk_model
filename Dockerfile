# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r margin_call_sim/requirements.txt

# Run Streamlit app
CMD ["streamlit", "run", "margin_call_sim/app.py"]