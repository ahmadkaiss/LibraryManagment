# 4. התקנת ספריות (Streamlit וכו')
#RUN pip install --no-cache-dir -r requirements.txt

## 5. הרצת האפליקציה
#CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
#

# Use the official Python image as base
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files to the container
COPY . .

# Install required Python packages
RUN pip install streamlit

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
