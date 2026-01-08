# 🚀 End-to-End MLOps: House Price Prediction Service

This repository demonstrates a complete MLOps pipeline, covering everything from machine learning model training and experiment tracking to containerization and automated CI/CD workflows.

### 🛠 Tech Stack
Language: Python 3.12

Machine Learning: Scikit-Learn (Linear Regression & Random Forest)

API Framework: FastAPI & Uvicorn

Containerization: Docker

Experiment Tracking: MLflow

CI/CD: GitHub Actions

Container Registry: Docker Hub

### 🏗 System Architecture
Experimentation: Models are trained using train.py, with all parameters and metrics (R2 Score) logged via MLflow.

Containerization: The application and its environment are packaged into a Docker image for consistent deployment.

Automation (CI): Every push to the main branch triggers a GitHub Action that builds and tests the Docker image.

Deployment (CD): The verified image is automatically pushed to Docker Hub, making it ready for production.

### 🚀 Quick Start (Usage)
You don't need Python or any libraries installed locally. You can run the entire service using Docker:

```
#Pull and run the image directly from Docker Hub
docker run -p 8080:80 sumeyyedemir/ml-api-image:v1
```

Once the container is running, test the prediction endpoint: http://localhost:8080/tahmin?m2=120

### 📊 Experiment Tracking with MLflow

To review model performances and compare different training runs:

``` mlflow ui ```

Then visit http://localhost:5000 in your browser.
