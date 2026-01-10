# 🚀 End-to-End MLOps: House Price Prediction Service

This repository demonstrates a production-grade MLOps pipeline, covering the entire lifecycle from data versioning and experiment tracking to automated testing and cloud deployment.

### 🛠 Tech Stack

* Language: Python 3.12

* Machine Learning: Scikit-Learn

* API Framework: FastAPI & Uvicorn

* Data Versioning: DVC (Data Version Control)

* Testing: Pytest & HTTPX

* Containerization: Docker

* Experiment Tracking: MLflow

* CI/CD: GitHub Actions

* Cloud Deployment: Google Cloud Run

* Container Registry: Docker Hub & Artifact Registry

### 🏗 System Architecture

1. Data Management: Training data is versioned using DVC, ensuring reproducibility across different environments.


2. Experimentation: Models are trained with train.py, logging metrics (R2 Score) and parameters via MLflow.


3. Quality Assurance: Automated unit tests using Pytest validate API logic and data validation before any deployment.


4. CI/CD Pipeline: Every push to main triggers a GitHub Action that:


   *  Lints and tests the code.

   *  Builds a Docker image.

   *  Pushes the verified image to Docker Hub and Google Artifact Registry.


5. Cloud Serving: The service is deployed on Google Cloud Run, providing a scalable, serverless production environment.

### 🚀 Live Demo

The service is currently live and can be reached at: 👉 https://house-price-api-324096341868.us-central1.run.app/docs

### 💻 Usage Guide

**Running with Docker (Local)**

You can run the entire service without installing Python:

```
# Pull and run the image directly from Docker Hub
docker run -p 8080:80 sumeyyedemir/ml-api-image:v1
```

Test the prediction: http://localhost:8080/tahmin?m2=120

**Data Versioning (DVC)**

To pull the latest data version:

```
dvc pull
```
**Running Tests**

To ensure the API is working correctly:

```
export PYTHONPATH=$PYTHONPATH:.
pytest
```

**Experiment Tracking (MLflow)**

To compare model runs:

```
mlflow ui
```

Then visit http://localhost:5000

### 📝 Key Features Added

✅ Automated Testing: CI/CD pipeline fails if tests don't pass, preventing buggy deployments.


✅ Serverless Deployment: Fully managed on Google Cloud with auto-scaling capabilities.


✅ Data-Code Lineage: Tracking which data version produced which model version using DVC.

