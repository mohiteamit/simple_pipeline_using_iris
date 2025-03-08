"""
Iris Classification API Module

This module loads the Iris classifier pipeline from disk, defines iris class mappings, 
and initializes a FastAPI application that serves predictions using the provided features.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

# Load the saved pipeline
try:
    with open("iris_pipeline.pkl", "rb") as f:
        pipeline = pickle.load(f)
except Exception as e:
    raise Exception(f"Error loading model: {e}")

# Define iris class names
iris_classes = {0: "setosa", 1: "versicolor", 2: "virginica"}

app = FastAPI(title="Iris Classification API")

class IrisInput(BaseModel):
    """
    Data model for iris flower features.

    Attributes:
        sepal_length (float): Length of the sepal.
        sepal_width (float): Width of the sepal.
        petal_length (float): Length of the petal.
        petal_width (float): Width of the petal.
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classification API"}

@app.post("/predict")
def predict(iris_input: IrisInput):
    try:
        features = np.array([[iris_input.sepal_length,
                              iris_input.sepal_width,
                              iris_input.petal_length,
                              iris_input.petal_width]])
        prediction = pipeline.predict(features)
        species = iris_classes[prediction[0]]
        return {"prediction": species}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
