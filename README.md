# Multiple Linear Regression - Startup Profit Prediction

## Project Overview
This project predicts the profit of a startup using a Multiple Linear Regression model. The application consists of a FastAPI backend for prediction and a Streamlit frontend for user interaction.

## Dataset
- 50_Startups.xls

## Input Features
- R&D Spend
- Administration
- Marketing Spend

## Target
- Profit

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Uvicorn
- Joblib

## Project Structure

```text
multiple-linear-regression-startup-profit-prediction/
│
├── backend/
│   ├── main.py
│   ├── train_model.py
│   ├── model.pkl
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│
├── 50_Startups.xls
├── README.md
└── .gitignore
```

## Installation

### Clone Repository

```bash
git clone https://github.com/WardaAhad/multiple-linear-regression-startup-profit-prediction.git
cd multiple-linear-regression-startup-profit-prediction
```

### Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Install Frontend Dependencies

```bash
cd ../frontend
pip install -r requirements.txt
```

## Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

## Run Frontend

```bash
cd frontend
streamlit run app.py
```

## Deployment

### Backend
- Railway
- FastAPI
- Uvicorn

### Frontend
- Streamlit

## Features

- Predict startup profit
- FastAPI REST API
- Interactive Streamlit UI
- Machine Learning model using Multiple Linear Regression
- Railway deployment support

## Author

**Warda Ahad**

Bachelor of Artificial Intelligence  
The Islamia University of Bahawalpur

## Deployment Update

Deployment refresh