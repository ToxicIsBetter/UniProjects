# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

# Load the dataset
heartdata = pd.read_csv("data-heart.csv")

# Separate features and target
X = heartdata.iloc[:, 0:13]  # Features
Y = heartdata.iloc[:, 13]    # Target

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=72)

# Standardize the feature values
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model using k=13
knn_best = KNeighborsClassifier(n_neighbors=13)
knn_best.fit(X_train, Y_train)
Y_pred = knn_best.predict(X_test)

# Evaluate the model
cm = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix:")
print(cm)

fscore = f1_score(Y_test, Y_pred)
print(f"F1 Score: {fscore:.2f}")

accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy: {accuracy:.2f}")
