# -*- coding: utf-8 -*-
"""loan-approval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mjgc_g4Wgj9tCPe2T3UJwi-Z2A1zlzRN

# **Loan Prediction**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
train=pd.read_csv('../input/loan-prediction/train_ctrUa4K.csv')
test=pd.read_csv('../input/loan-prediction/test_lAUu6dG.csv')

df=pd.DataFrame(data=train)
df.head()

index = df. index
number_of_rows = len(index)
print(number_of_rows)

#get correlations of each features in dataset
corrmat = df.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
#plot heat map
g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")

df.dtypes

sns.heatmap(df.isnull())

df["Gender"].mode()

df["Gender"].fillna("Male",inplace=True)

df["Married"].mode()

df["Married"].fillna("Yes",inplace=True)

df["Self_Employed"].mode()

df["Self_Employed"].fillna("No",inplace=True)

m=df["LoanAmount"].median()

df["LoanAmount"].fillna(m,inplace=True)

df["Loan_Amount_Term"].mode()

df["Loan_Amount_Term"].fillna(360.0,inplace=True)

df["Credit_History"].mode()

df["Credit_History"].fillna(1.0,inplace=True)

df.Dependents.fillna("0",inplace=True)

df.dtypes

depend  = {'1': 1,'0':0,'2':2,'3+':3} 
df.Dependents = [depend[item] for item in df.Dependents] 
df.head()

df["Dependents"].mode()

#df.dropna(axis=0,inplace=True)

sns.heatmap(df.isnull())

df.drop('Loan_ID',inplace=True,axis=1)
#df.drop('Dependents',inplace=True,axis=1)

approval  = {'Y': 1,'N':0} 
df.Loan_Status = [approval[item] for item in df.Loan_Status] 
df.head()

gender  = {'Female': 1,'Male':0} 
df.Gender = [gender[item] for item in df.Gender] 
df.head()

married  = {'Yes': 1,'No':0} 
df.Married = [married[item] for item in df.Married] 
df.head()

education = {'Graduate': 1,'Not Graduate':0} 
df.Education = [education[item] for item in df.Education] 
df.head()

prop = {'Rural': 0,'Urban':2,'Semiurban':1} 
df.Property_Area = [prop[item] for item in df.Property_Area] 
df.head()

selfemp = {'Yes': 1,'No':0} 
df.Self_Employed = [selfemp[item] for item in df.Self_Employed] 
df.head()

fea_normalize=['Dependents','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Property_Area']

for fea in fea_normalize:
    df[fea]=(df[fea])/(df[fea].max())

df.head()

x_train, x_test, y_train, y_test = train_test_split(df.drop('Loan_Status',axis=1,inplace=False), df['Loan_Status'], test_size=0.8, random_state=43)

x_train.head()

y_train.head()

#df.dtypes

from sklearn.metrics import f1_score, accuracy_score, confusion_matrix

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth' : range(4,25),
    'min_samples_leaf' : range(20,200,10),
    'min_samples_split' : range(20,200,10),
    'criterion' : ['gini','entropy'] 
}
n_folds = 5

rd=RandomForestClassifier(random_state=np.random.randint(0,100))
grid = GridSearchCV(rd, param_grid, cv = n_folds, return_train_score=True,verbose=3)

#grid.fit(x_train,y_train)

#grid.best_params_

classifier=RandomForestClassifier(n_estimators=12,criterion='gini',random_state=43,max_features='auto',max_depth=7,min_samples_leaf=7,min_samples_split=20)
classifier.fit(x_train,y_train)
preds=classifier.predict(x_test)

accuracy=accuracy_score(y_test,preds)
accuracy

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

best_tree=DecisionTreeClassifier(criterion='gini',max_depth=4,min_samples_leaf=20,min_samples_split=80,random_state=np.random.randint(0,100))
best_tree.fit(x_train,y_train)
y_pred_best=best_tree.predict(x_test)

accuracy=accuracy_score(y_test,y_pred_best)
accuracy







cfm=confusion_matrix(y_test,preds)
f, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cfm, annot=True, linewidth=0.7, linecolor='cyan', fmt='g', ax=ax, cmap="BuPu")
plt.title('Classification Confusion Matrix')
plt.xlabel('Y predict')
plt.ylabel('Y test')
plt.show()

test.head()

sns.heatmap(test.isnull())

test.Dependents.fillna("0",inplace=True)
depend  = {'1': 1,'0':0,'2':2,'3+':3} 
test.Dependents = [depend[item] for item in test.Dependents] 
test.head()

test["Gender"].mode()



test["Gender"].fillna("Male",inplace=True)

test["Self_Employed"].mode()

test["Self_Employed"].fillna("No",inplace=True)

m=test["LoanAmount"].median()
m

test["LoanAmount"].fillna(m,inplace=True)

test["Loan_Amount_Term"].mode()

test["Loan_Amount_Term"].fillna(360.0,inplace=True)

test["Credit_History"].mode()

test["Credit_History"].fillna(1.0,inplace=True)

sns.heatmap(test.isnull())

#test.dropna(axis=0,inplace=True)

test2=test.drop("Loan_ID",axis=1,inplace=False)
test2.head()

selfemp = {'Yes': 1,'No':0} 
test2.Self_Employed = [selfemp[item] for item in test2.Self_Employed] 
#test2.head()

prop = {'Rural': 0,'Urban':2,'Semiurban':1} 
test2.Property_Area = [prop[item] for item in test2.Property_Area] 
#test2.head()

education = {'Graduate': 1,'Not Graduate':0} 
test2.Education = [education[item] for item in test2.Education] 
#test2.head()

married  = {'Yes': 1,'No':0} 
test2.Married = [married[item] for item in test2.Married] 
#test2.head()

gender  = {'Female': 1,'Male':0} 
test2.Gender = [gender[item] for item in test2.Gender] 
#test2.head()



preds=best_tree.predict(test2)

preds

loan  = {1: 'Y',0:'N'} 
preds = [loan[item] for item in preds] 
#preds

test3=pd.DataFrame()
test3["Loan_ID"]=test["Loan_ID"]

test3["Loan_Status"]=preds

test3.to_csv('submitfinal.csv', index=False)

import pickle
# open a file, where you ant to store the data
file = open('loan_approval_random_forest_classifier.pkl', 'wb')

# dump information to that file
pickle.dump(classifier, file)