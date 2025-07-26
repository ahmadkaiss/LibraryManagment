# 4. התקנת ספריות (Streamlit וכו')
#RUN pip install --no-cache-dir -r requirements.txt

## 5. הרצת האפליקציה
#CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
#

# Use the official Python image as base
FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set working directory inside the container
WORKDIR /app

# Clone your GitHub repo
RUN git clone https://github.com/ahmadkaiss/LibraryManagment .

# Install required Python packages
RUN pip install streamlit

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
