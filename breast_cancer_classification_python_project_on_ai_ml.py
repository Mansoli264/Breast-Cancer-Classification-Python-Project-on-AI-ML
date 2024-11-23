# -*- coding: utf-8 -*-
"""Breast Cancer Classification Python Project on AI/ML

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LgwR1_YVM55DFhB2TVtwpxkzpsTbPoFD
"""

# prompt: import pandas as pd
import numpy as np
import pandas as pd
# Import the base sklearn module
import sklearn#FIXED: Added the import statement for sklearn
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Assuming 'pandas_read_csv' was intended, correcting the typo
from pandas import read_csv as pandas_read_csv #FIXED: changed padas_read_csv to read_csv
from pandas import read_csv

from google.colab import drive
drive.mount('/content/drive')

"""Data Collection & Processing"""

# loading the data from sklearn
breast_cancer_dataset = sklearn.datasets.load_breast_cancer()

print(breast_cancer_dataset)

# loading the data to a data frame
data_frame = pd.DataFrame(breast_cancer_dataset.data, columns = breast_cancer_dataset.feature_names)

# print the first 5 rows of the dataframe
data_frame.head()

# adding the 'target' column to the dataframe
data_frame['label'] = breast_cancer_dataset.target
#

# print last 5 rows of the dataframe
data_frame.tail()

# number of rows and columns in the dataset
data_frame.shape

# getting some information about the data
data_frame.info()

# checking for missing value
data_frame.isnull().sum()

# statistical measures about the data
data_frame.describe()

# checking the distribution of target variable
data_frame['label'].value_counts()

"""1..> Benign
0..>Malignan
"""

data_frame.groupby('label').mean()
#

"""Separating the features and target"""

## Code adapted from https://github.com/sachidas1818/breast_cancer_classification
# License: MIT (LICENSE)

X = data_frame.drop(columns='label', axis=1)
Y = data_frame['label']

print(X)

print(Y)

"""Spliting the data into training data & Testing data"""

X_train, X_train, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Code adapted from https://github.com/sachidas1818/breast_cancer_classification
# License: MIT (LICENSE)

# Split the data into training and testing sets (e.g., 80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training"""

# Set up and train the Logistic Regression model
model = LogisticRegression

# Code adapted from https://github.com/sachidas1818/breast_cancer_classification
# License: MIT(LICENSE)

# Define X as the data and y as the labels
X = breast_cancer_dataset.data
y = breast_cancer_dataset.target

# Ensure consistent split for X and y with 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Double-check the shapes
print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_test shape: {y_test.shape}")

model = LogisticRegression()

# Train the model using the training data
model.fit(X_train, y_train)

"""Model Evaluation

Accuracy Score
"""

# accuracy on training data
X_train_prediction= model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy on training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy on test data : ', test_data_accuracy)

"""Building a Predictive System"""

input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259
)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one datapoint

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Breast cancer is Malignant')

else:
  print('The Breast Cancer is Benign')
