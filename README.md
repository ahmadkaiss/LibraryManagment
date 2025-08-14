# 📚 Library Management System

Welcome to the **Library Management System**!
This project is a **Python-based** application for managing books, users, and borrowing/return records.
It supports both **CLI (Command-Line Interface)** and **Web Interface** modes, and is fully containerized with **Docker** for consistent deployment.
You can also deploy it to **AWS** using **ECR** (for storing images) and **CloudFormation** (for infrastructure).

---

## **Part 1 – CLI Application**

### 🌟 Overview

The CLI application allows library administrators to manage all core operations directly from the terminal:

* Add, remove, and edit books
* Register and remove users
* Borrow and return books
* View library statistics
* Search for books by title, author, or genre

Perfect for **lightweight usage** or environments without a web browser.

---

### ✨ Features (CLI)

* 📖 **Add Books** – Create book records with title, author, genre, and availability
* 🗑 **Remove Books** – Delete books from the database
* 📝 **Edit Books** – Update book details
* 👤 **Manage Users** – Add or remove library members
* 📥 **Borrow Books** – Assign books to users if available
* 📤 **Return Books** – Mark books as returned and available again
* 📊 **Statistics** – View total books, available books, and registered users
* 🔍 **Search Books** – Find books quickly by keyword

---

### 📂 Folder Structure (CLI)

```
library-management/
├── main.py               # CLI entry point
├── book_functions.py     # Book-related logic
├── user_functions.py     # User-related logic
```

---

## **Part 2 – Web Application**

### 🌟 Overview

The web interface is built with **Flask** and **Jinja2** templates, providing a clean, browser-based UI for managing books and users.

Admins can:

* Add, edit, and remove books
* Manage user records
* Borrow/return books through forms
* View statistics in an interactive dashboard

---

### ✨ Features (Web)

* 📚 **Book Management** – Full CRUD operations from the browser
* 👥 **User Management** – Add, remove, and edit users
* ✅ **Borrow/Return** – Web-based transaction forms
* 📊 **Dashboard** – Live statistics on books and members
* 🎨 **Clean UI** – HTML/CSS templates for a professional look

---

### 📂 Project Structure (Web)

```
library-management/
├── app.py                # Flask web app
├── templates/            # HTML templates
├── static/               # Static files (CSS/images)
├── Dockerfile            # Docker build instructions
├── cloudformation.yaml   # AWS deployment template
└── README.md             # Project documentation
```

---

## 🐳 **Running with Docker**

**Build the Docker image:**

```bash
docker build -t library-app .
```

**Run the container:**

```bash
docker run -p 5000:5000 library-app
```

---

## ☁ **AWS Deployment**

This application can be deployed on AWS using **ECR** and **CloudFormation**.

### 🧱 Prerequisites

* ✅ AWS account
* ✅ Docker installed
* ✅ AWS CLI configured
* ✅ IAM permissions for ECR, EC2, CloudFormation

---
### 🔑 Step 0: Connect to AWS

Before pushing images or deploying, set your AWS credentials:

$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"
$env:AWS_SESSION_TOKEN="your_session_token"  
$env:AWS_DEFAULT_REGION="us-east-1"

Verify the connection:

aws sts get-caller-identity


### 📦 Step 1: Push Image to ECR

**Authenticate Docker with ECR:**

```bash
aws ecr get-login-password --region us-east-1 | \
docker login --username AWS --password-stdin <account_id>.dkr.ecr.us-east-1.amazonaws.com
```

**Create an ECR Repository:**

```bash
aws ecr create-repository --repository-name library-management --region us-east-1
```

**Tag the image:**

```bash
docker tag library-app:latest <account_id>.dkr.ecr.us-east-1.amazonaws.com/library-management:latest
```

**Push the image:**

```bash
docker push <account_id>.dkr.ecr.us-east-1.amazonaws.com/library-management:latest
```

---

### 🌐 Step 2: Deploy via CloudFormation

1. Upload `cloudformation.yaml` to **AWS CloudFormation**.
2. Wait for the stack to complete.

---

### 🖥 Step 3: Access the Application

Retrieve the **ALB URL** from the stack’s **Outputs** tab.

---

## 🛠 **Technologies Used**

* Python 3.10
* Flask (Web)
* HTML / Jinja2
* Docker
* AWS ECR, EC2, ALB, CloudFormation

---

## 📜 License

This project is licensed under the **MIT License**.
