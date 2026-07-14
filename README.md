# Multiple Linear Regression - Startup Profit Prediction

## Project Overview

This project is a Machine Learning based Startup Profit Prediction System that predicts the expected profit of a startup using a **Multiple Linear Regression** model.

The application is developed as an end-to-end ML deployment project consisting of:

* **FastAPI Backend** for serving machine learning predictions through REST API
* **Streamlit Frontend** for an interactive user interface
* **Railway Deployment** for hosting the backend API

The user provides startup details such as R&D Spend, Administration Cost, Marketing Spend, and State. The trained model then predicts the expected startup profit.

---

# Dataset

## Dataset Name

**50_Startups Dataset**

The dataset contains information about different startups and their expenses along with their achieved profit.

## Dataset Features

* R&D Spend
* Administration
* Marketing Spend
* State
* Profit

---

# Machine Learning Problem

## Type

**Supervised Machine Learning - Regression**

## Algorithm Used

**Multiple Linear Regression**

## Objective

To build a regression model that learns the relationship between startup expenses and profit, then predicts future startup profitability.

---

# Input Features

The model uses the following input features:

* R&D Spend
* Administration
* Marketing Spend
* State

## State Encoding

Categorical State values are converted using One-Hot Encoding:

* state_florida
* state_new_york

California is treated as the baseline category.

---

# Target Variable

The model predicts:

```
Profit
```

---

# Technologies Used

## Programming Language

* Python

## Data Processing

* Pandas
* NumPy

## Machine Learning

* Scikit-learn
* Multiple Linear Regression

## Backend Development

* FastAPI
* Uvicorn
* Joblib

## Frontend Development

* Streamlit

## Deployment

* Railway

## Version Control

* Git
* GitHub

---

# Project Structure

```
multiple-linear-regression-startup-profit-prediction/

│
├── backend/
│   │
│   ├── main.py
│   ├── train_model.py
│   ├── model.pkl
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── app.py
│   └── requirements.txt
│
├── 50_Startups.xls
├── README.md
└── .gitignore
```

---

# Installation and Setup

## Clone Repository

```bash
git clone https://github.com/WardaAhad/multiple-linear-regression-startup-profit-prediction.git

cd multiple-linear-regression-startup-profit-prediction
```

---

# Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
uvicorn main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI provides automatic Swagger documentation.

Open:

```
http://127.0.0.1:8000/docs
```

Available Endpoint:

```
POST /predict
```

---

# Frontend Setup

Open a new terminal:

```bash
cd frontend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# API Request Example

## Endpoint

```
POST /predict
```

## Request Body

```json
{
  "rd_spend": 165349.2,
  "administration": 136897.8,
  "marketing_spend": 471784.1,
  "state_florida": 0,
  "state_new_york": 1
}
```

---

# Prediction Response

```json
{
  "predicted_profit": 193197.05
}
```

---

# Deployment

## Backend Deployment

The FastAPI backend is deployed on:

**Railway**

Live API:

```
https://multiple-linear-regression-startup-profit-predic-production.up.railway.app
```

API Endpoint:

```
/predict
```

---

# Application Features

✅ Startup profit prediction
✅ Multiple Linear Regression model
✅ FastAPI REST API
✅ Interactive Streamlit UI
✅ One-Hot Encoding for categorical data
✅ Trained ML model integration
✅ Cloud deployment using Railway
✅ Real-time prediction system

---

# Sample Prediction

### Input

```
R&D Spend:
165349.20

Administration:
136897.80

Marketing Spend:
471784.10

State:
New York
```

### Output

```
Predicted Profit:
$193,197.05
```

---

# Future Improvements

* Add more regression algorithms for comparison
* Add model performance metrics
* Add data visualization dashboard
* Deploy Streamlit frontend online
* Add user authentication

---

# Author

**Warda Ahad**

Bachelor of Artificial Intelligence
The Islamia University of Bahawalpur

---

# License

This project is created for learning, portfolio, and educational purposes.
