import streamlit as st
import pickle
import numpy as np

# Load the saved pipeline
with open("iris_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

# Mapping of iris class indices to names
iris_classes = {0: "setosa", 1: "versicolor", 2: "virginica"}

st.title("Iris Flower Classification")
st.write("Enter the iris features to predict the species:")

# User inputs for iris features
sepal_length = st.number_input("Sepal Length", min_value=0.0, max_value=10.0, value=5.1)
sepal_width  = st.number_input("Sepal Width", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length", min_value=0.0, max_value=10.0, value=1.4)
petal_width  = st.number_input("Petal Width", min_value=0.0, max_value=10.0, value=0.2)

if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = pipeline.predict(features)
    st.write("Predicted Iris Species:", iris_classes[prediction[0]])
