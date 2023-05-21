#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:12:21 2023

@author: vasanthdhanagopal
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dia = pd.read_csv("/Users/vasanthdhanagopal/Desktop/360DigiTMG/2.DataScience-Sampath/17.Data Mining-DecisionTree/Datasets_DTRF/Diabetes.csv")
dia.info()
dia.head()
dia.isnull().sum
dia.describe()
dia.columns

from sklearn import preprocessing
  
# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()
  
# Encode labels in column 'species'.
dia[' Class variable']= label_encoder.fit_transform(dia[' Class variable'])
  
dia[' Class variable'].unique()

# Input and Output Split
predictors = dia.loc[:, dia.columns!=' Class variable']

target = dia[' Class variable']
sns.heatmap(dia.corr())


# Train Test partition of the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size = 0.2, random_state=0)


from sklearn.preprocessing import StandardScaler
scaling_x=StandardScaler()
X_train=scaling_x.fit_transform(x_train)
X_test=scaling_x.transform(x_test)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
rfc.score(X_test, y_test)


from sklearn.metrics import confusion_matrix
mat = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(mat, annot=True)


from sklearn.metrics import classification_report
target_names = ['Diabetes', 'Normal']
print(classification_report(y_test, y_pred, target_names=target_names))

# Train the Regression DT
from sklearn import tree
regtree = tree.DecisionTreeRegressor(max_depth = 3)
regtree.fit(X_train, y_train)

# Prediction
test_pred = regtree.predict(X_test)
train_pred = regtree.predict(X_train)

