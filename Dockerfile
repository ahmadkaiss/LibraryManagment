FROM python:3.10-slim

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Clone your repo
RUN git clone https://github.com/ahmadkaiss/LibraryManagment .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]

