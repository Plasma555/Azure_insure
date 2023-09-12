  Insurance Premium Prediction Model

This GitHub repository contains the code and resources for an insurance premium prediction model. The project encompasses various aspects, including data exploration, model development, deployment, and the creation of a real-time endpoint on Azure. Additionally, exploratory analysis has been conducted to gain insights into the dataset. This README will guide you through the repository and provide instructions for getting started.

 Table of Contents

- [Introduction](#introduction)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Development](#model-development)
- [Azure Real-Time Endpoint](#azure-real-time-endpoint)
- [Heroku Deployment](#heroku-deployment)


 Introduction

This project aims to predict insurance premiums for policyholders based on various features such as age, gender, location, and more. The model developed here has been deployed as a web application on Heroku using Flask, allowing users to input their information and receive insurance premium estimates. Additionally, a real-time endpoint has been created on Microsoft Azure for programmatic access to the model.

## Exploratory Data Analysis

Before diving into model development, extensive exploratory data analysis (EDA) has been conducted. The `eda/` directory contains Jupyter Notebook files and Python scripts for EDA. Using Pandas, NumPy, Matplotlib, Plotly, and Seaborn, we explored the dataset to gain insights into its structure, identify patterns, and understand relationships between variables.

## Model Development

The core of this project is model development. After EDA, the dataset was preprocessed and transformed. Numerical features were scaled, and categorical features were encoded. Multiple machine learning algorithms were employed, including Linear Regression, Decision Tree Regressor, Random Forest Regressor, Gradient Boosting Regressor, XGBoost Regressor, and K-Nearest Neighbors (KNN).

Model performance was evaluated using metrics such as Root Mean Square Error (RMSE) and R-squared (R^2). The model with the best performance was selected, serialized into a pickle file, and made available for future use.

## Azure Real-Time Endpoint

A real-time endpoint has been created on Microsoft Azure for the selected model. This endpoint allows for programmatic access to the model via REST API requests, making it accessible and scalable for various applications.

## Heroku Deployment

The selected model has also been deployed as a user-friendly web application on Heroku using Flask. This deployment provides an intuitive interface for users to input their information and obtain insurance premium estimates.

## Heroku Link- https://azure-insure-14e23255c561.herokuapp.com/

