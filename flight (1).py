# -*- coding: utf-8 -*-
"""flight.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nC82Wmt44dNRXLnZIvmEhb5Oj4bRQSog
"""

# Commented out IPython magic to ensure Python compatibility.
import torch
import numpy as np 
import pandas as pd
import matplotlib as plt
import math
import matplotlib as plt
# %matplotlib inline

import csv
with open('flights_train.csv') as f:
    reader = csv.reader(f)
    h_names = next(reader)
h_names

df_test = pd.read_csv('flights_test.csv')

df_test.head(5)

df = pd.read_csv('flights_train.csv')
df.head(5)

for nam in h_names:
  a = df[[nam]].isnull().values().any()
  print(nam, a)

df = df.drop('FIRST_DEP_TIME', 1)
df.head()

df_test = df_test.drop('FIRST_DEP_TIME', 1)
df_test.head(3)
kk = 'ORIGIN'
print(df[kk].value_counts())
print('length:')
print(len(df[kk].value_counts))

outl = df['ARR_DELAY'] < 300
df_new = df[outl]
df = df_new
print('length:')
print(len(df))

df.shape

df_test.shape

df_train = df
one_hot = pd.get_dummies(df_train['DAY_OF_WEEK'])
df_train = df_train.drop('DAY_OF_WEEK', axis = 1)
df_train = df_train.join(one_hot)
df_train.head(5)
print(df_train.shape)
df_train.head(5)

df_train = df_train.rename(columns={1: 'Mon', 2: 'Tue',3: 'Wed',4: 'Thurs',5: 'Fri',6: 'Sat',7: 'Sun'})
df_train.head(2)
column_names = df_train.columns.values
print(column_names)

# do the same for df_test
df_test = df_test.rename(columns={1: 'Mon', 2: 'Tue',3: 'Wed',4: 'Thurs',5: 'Fri',6: 'Sat',7: 'Sun'})
df_test.head(2)
column_names = df_test.columns.values
print(column_names)

arr_one_hot = ['AIRLINE_ID', 'UNIQUE_CARRIER']
for x in arr_one_hot:
  one_hot = pd.get_dummies(df_train[x])
  df_train = df_train.drop(x, 1)
  df_train = df_train.join(one_hot)
  print(x)
  print(df_train.shape)

df_train.head(5)

arr_one_hot_test = ['AIRLINE_ID',
               'UNIQUE_CARRIER'
              ]
for x in arr_one_hot_test:
    one_hot_test = pd.get_dummies(df_test[x])
    df_test = df_test.drop(x,1)
    df_test = df_test.join(one_hot_test)
    print(x)
    print(df_test.shape)

df_test.head(5)

df_train.head(5)

df1 = df_train
df1['month'] = pd.DatetimeIndex(df1['FL_DATE']).month
column_names = df1.column,values
print(column_names)
print(df1.shape)

df2 = df_test
dfs['month'] = pd.DatetimeIndex(df2['FL_DATE']).month
column_names = df2.columns.values
print(column_names)
print(df2.shape)

# convert month to hot coding
one_hot = pd.get_dummies(df1['month'])
df1 = df1.drop('month',axis=1)
df1 = df1.join(one_hot)
# one_hot.head()
df1.head(5)
print(df_train.shape)
df1.head(5)



# do same for df_test
one_hot_test = pd.get_dummies(df2['month'])
df2 = df2.drop('month',axis=1)
df2 = df2.join(one_hot_test)
# one_hot.head()
df2.head(5)
print(df2.shape)
df2.head(5)

column_names = df1.columns.values
print(column_names)
print("Number of att: ", len(column_names))
print(df1.shape)

column_names = df2.columns.values
print(column_names)
print("Number of att: ", len(column_names))
print(df2.shape)

df =df1
# Note that we also delete FL_DATE
remov_att = ['FL_NUM',
             'FL_DATE',
               'ORIGIN',  
               'ORIGIN_CITY_MARKET_ID',
               'ORIGIN_CITY_NAME',
               'DEST_CITY_MARKET_ID',
               'DEST',
               'DEST_CITY_NAME',
               'CRS_DEP_TIME',
               'DISTANCE',
              'DISTANCE_GROUP',
            'DEST_STATE_ABR',
            'ORIGIN_STATE_ABR'
            ]
for x in remov_att:
    df = df.drop(x,1)
    print(x)
    print(df.shape)

df.head(5)

df_test =df2
remov_att = ['FL_NUM',
             'FL_DATE',
               'ORIGIN',  
               'ORIGIN_CITY_MARKET_ID',
               'ORIGIN_CITY_NAME',
               'DEST_CITY_MARKET_ID',
               'DEST',
               'DEST_CITY_NAME',
               'CRS_DEP_TIME',
               'DISTANCE',
              'DISTANCE_GROUP',
            'DEST_STATE_ABR',
            'ORIGIN_STATE_ABR'
            ]
for x in remov_att:
    df_test = df_test.drop(x,1)
    print(x)
    print(df_test.shape)

df_test.head(5)

x_train_df = df.drop('ARR_DELAY',axis=1)
x_train_df = x_train_df.drop('UID',axis=1)
r_train_df = df[['ARR_DELAY']]


x_test_df = df_test
x_test_df = x_test_df.drop('UID',axis=1)


print(x_train_df.shape)
print(r_train_df.shape)
print(x_test_df.shape)


print("PRINTING TRAINING DATA:")
column_names = x_train_df.columns.values
print(column_names)
print("Number of att: ", len(column_names))
print(x_train_df.iloc[:, 0:18].head(3))
print(x_train_df.iloc[:, 18:36].head(3))
print(x_train_df.iloc[:, 36:54].head(3))
print(x_train_df.iloc[:, 54:72].head(3))
print(x_train_df.iloc[:, 72:90].head(3))
print(x_train_df.iloc[:, 90:108].head(3))
# print(df.iloc[:, 0:18].head(3))
print(x_train_df.shape)



print("PRINTING TEST DATA:")
column_names = x_test_df.columns.values
print(column_names)
print("Number of att: ", len(column_names))
print(x_test_df.iloc[:, 0:18].head(3))
print(x_test_df.iloc[:, 18:36].head(3))
print(x_test_df.iloc[:, 36:54].head(3))
print(x_test_df.iloc[:, 54:72].head(3))
print(x_test_df.iloc[:, 72:90].head(3))
print(x_test_df.iloc[:, 90:108].head(3))
# print(df.iloc[:, 0:18].head(3))
print(x_test_df.shape)


# normazling
# import sklearn
# x_train = x_train_df.values
# x_train = sklearn.preprocessing.normalize(x_train)
# x_train.shape
# print(x_train)
x_train = x_train_df.values
x_train.shape


r_train = r_train_df.values
y_train=r_train
# y_train= y_train.transpose()
r_train.shape


x_test_df = x_test_df.values
x_test_df.shape


# import sklearn.decomposition as skd

# # .fit computes the principal components  (n_components of them)
# # The columns of W are the eigenvectors of the covariance matrix of X
# pca = skd.PCA(n_components = 20)
# skd.PCA.fit(pca,x_train)
# W1 = pca.components_
# W = W1.transpose()
# Z = pca.transform(x_train)
# print(W)
# print(Z)


import torch 
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib as plt

class Net(torch.nn.Module):
  def __init__(self, n_feature, n_hidden, n_output):
    super(Net, self).__init__()
    self.hidden = torch.nn.Linear(n_feature, n_hidden)
    self.predict = torch.nn.Linear(n_hidden, n_output)
  
  def forward(self, x):
    x = F.relu(self.hidden(x))
    x = self.predict(x)
    return x

    ### Fully connected DNN 

    '''
    class Net(torch.nn.Module):
      super(Net, self).__init__()
      self.hidden_a = torch.nn.Linear(n_feature, n_hidden_1)
      self.hidden_b = torch.nn.Linear(n_hidden_1, n_hidden_2)
      self.predict = torch.nn.Linear(n_hidden_2, n_output)
    
    def forward(self, x):
      x = F.tanh(self.hidden_a(x))
      x = F.tanh(self.hidden_b(x))
      x = self.predict(x)
      return x

    '''
  
  model = Net(n_feature = 46, n_hidden = 15, n_output = 1)
  print(model)

  optimizer = torch.optim.SGD(net.parameters(), lr= 0.5, momentum = 0.9)
  loss_func = torch.nn.MSELoss()

import torch 
import torch.nn as nn
import matplotlib.pyploy as plt
import numpy as np 

num_epochs = 20
learning_rate = 0.001
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)

# x_train = np.array([[3.3,1,1], [4.4,1,1], [5.5,2,2], [6.71,2,2], [6.93,2,2]], dtype=np.float32)

# y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694]], dtype=np.float32)

for epoch in range(num_epochs):
  inputs = torch.from_numpy(x_train)
  targets = torch.from_numpy(y_train)

  outputs = Variable(torch.from_numpy(x_train).float(), requires_grad = True)
  targets = Variable(torch.from_numpy(y_train).float(), requires_grad = True)

  outputs = mode(inputs)
  loss = criterion(outputs, targets)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

  if(epoch+1)%5 == 0:
    print('Epoch [ {}/ {}], Loss : {:.4f}'.format(epoch+1, num_epochs, loss.item()))

# Commented out IPython magic to ensure Python compatibility.
## For Regression

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x_train,y_train)

# Make predictions using the testing set
y_pred = regr.predict(x_train)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
y_test = y_train
print("Mean squared error: %.2f"
#       % mean_squared_error(y_test, y_pred))

for i in range(0,5):
    prediction = y_pred[i] 
    label = y_train[i]
    print("prediction = {0},  label = {1}".format(prediction,label))


    
def pol_regress(x_tr,y_tr,x_tes,y_tes,deg):
    
    poly = PolynomialFeatures(degree=deg)
    X_transform_ = poly.fit_transform(x_tr)
    regression = linear_model.LinearRegression()
    regression.fit(X_transform_,y_tr)

    # Make predictions using the testing set
    X_transform_test = poly.fit_transform(x_tes)
    y_pred = regression.predict(X_transform_test)

#     # The coefficients
#     print('Coefficients: \n', regression.coef_)
#     # The mean squared error

    print("Mean squared error for test: %.2f"
#           % mean_squared_error(y_tes, y_pred))
    transform_ = poly.fit_transform(x_tr)
    y_train_pred = regression.predict(transform_)
    print("Mean squared error for training: %.2f"
#           % mean_squared_error(y_tr, y_train_pred))
    

for i in range(0,5):
    prediction = y_pred[i] 
    label = y_train[i]
    print("prediction = {0},  label = {1}".format(prediction,label))


def lin_regress(x_tr,y_tr,x_tes,y_tes):
    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(x_tr,y_tr)

    # Make predictions using the testing set
    y_pred = regr.predict(x_tes)

    # The coefficients
#     print('Coefficients: \n', regr.coef_)
    # The mean squared error
    
    print("Mean squared error for test: %.2f"
#           % mean_squared_error(y_tes, y_pred))
    
    y_train_pred = regr.predict(x_tr)
    print("Mean squared error for training: %.2f"
#           % mean_squared_error(y_tr, y_train_pred))
    
    linear_regression_test_mse.append(mean_squared_error(y_tes, y_pred))



linear_regression_test_mse=[]
from sklearn.model_selection import KFold
X =x_train
y=r_train
print(y.shape)
print(X.shape)
kf = KFold(n_splits=10)
kf.get_n_splits(X)

# print(kf)  
KFold(n_splits=10, random_state=None, shuffle=False)
for train_index, test_index in kf.split(X):
#     print("TRAIN:", train_index, "TEST:", test_index)
#     print(test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    lin_regress(X_train,y_train,X_test,y_test)
    
    
    
print('Mean Test MSE= ', np.mean(linear_regression_test_mse))




from sklearn.linear_model import Ridge
# def ridge_regression(data, predictors, alpha, models_to_plot={}):
#     #Fit the model
#     ridgereg = Ridge(alpha=alpha,normalize=True)
#     ridgereg.fit(data[predictors],data['y'])
#     y_pred = ridgereg.predict(data[predictors])
    
def ridge_regress(x_tr,y_tr,x_tes,y_tes):
    # Create linear regression object
    regr = Ridge(alpha=5.0,fit_intercept=False)

    # Train the model using the training sets
    regr.fit(x_tr,y_tr)

    # Make predictions using the testing set
    y_pred = regr.predict(x_tes)

    # The coefficients
#     print('Coefficients: \n', regr.coef_)
    # The mean squared error
    
    print("Mean squared error for test: %.2f"
#           % mean_squared_error(y_tes, y_pred))
    
    y_train_pred = regr.predict(x_tr)
    print("Mean squared error for training: %.2f"
#           % mean_squared_error(y_tr, y_train_pred))
    ridge_regression_test_mse.append(mean_squared_error(y_tes, y_pred))


    
ridge_regression_test_mse=[]
from sklearn.model_selection import KFold
X =x_train
y=r_train
print(y.shape)
print(X.shape)
kf = KFold(n_splits=10)
kf.get_n_splits(X)

# print(kf)  
KFold(n_splits=10, random_state=None, shuffle=False)
for train_index, test_index in kf.split(X):
#     print("TRAIN:", train_index, "TEST:", test_index)
#     print(test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    ridge_regress(X_train,y_train,X_test,y_test)

print('Mean Test MSE= ', np.mean(ridge_regression_test_mse))



from sklearn.linear_model import Lasso

    
def lasso_regress(x_tr,y_tr,x_tes,y_tes):
    # Create linear regression object
    regr = Lasso(alpha=1.0,fit_intercept=False)

    # Train the model using the training sets
    regr.fit(x_tr,y_tr)

    # Make predictions using the testing set
    y_pred = regr.predict(x_tes)

    # The coefficients
#     print('Coefficients: \n', regr.coef_)
    # The mean squared error
    
    print("Mean squared error for test: %.2f"
#           % mean_squared_error(y_tes, y_pred))
    
    y_train_pred = regr.predict(x_tr)
    print("Mean squared error for training: %.2f"
#           % mean_squared_error(y_tr, y_train_pred))
    
    lasso_regression_test_mse.append(mean_squared_error(y_tes, y_pred))



lasso_regression_test_mse=[]
from sklearn.model_selection import KFold
X =x_train
y=r_train
print(y.shape)
print(X.shape)
kf = KFold(n_splits=10)
kf.get_n_splits(X)

# print(kf)  
KFold(n_splits=10, random_state=None, shuffle=False)
for train_index, test_index in kf.split(X):
#     print("TRAIN:", train_index, "TEST:", test_index)
#     print(test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    lasso_regress(X_train,y_train,X_test,y_test)
    
    
print('Mean Test MSE= ', np.mean(lasso_regression_test_mse))



import sklearn
nalpha = 100
alphas = np.logspace(-3,1,nalpha)

alphas1, coeffs, _ = sklearn.linear_model.lasso_path(X, y, alphas=alphas)


print(alphas1)
print(alphas1.shape)
print(coeffs)
print(coeffs.shape)
coeffs=coeffs.reshape((46,100)) 
print(coeffs.shape)



plt.figure(figsize = (16, 7))
plt.semilogy(alphas1, coeffs.T)
plt.grid()
plt.legend(column_names , loc = ' upper right', prop = {'size' :6 })



model = linear_model.Lasso(warm_start=False)

# Regularization values to test
nalpha = 40
alphas = np.logspace(-3,5,nalpha)
mse_list=[]
# Compute the lasso path for the split
for a in alphas:

    # Fit the model on the training data
    model.alpha = a
    model.fit(X,y)

    y_pred = model.predict(X)
    mse = np.mean((y_pred-y)**2)
    mse_list.append(mse)
    
print(mse_list)


plt.semilogx(alphas, mse_list)

plt.xlabel('alpha')
plt.ylabel('Train MSE')
plt.grid()
plt.show()

# Create a k-fold cross validation object
nfold = 10
kf = sklearn.model_selection.KFold(n_splits=nfold,shuffle=True)

# Create the LASSO model.  We use the `warm start` parameter so that the fit will start at the previous value.
# This speeds up the fitting.
model = linear_model.Lasso(warm_start=True)

# Regularization values to test
nalpha = 40
alphas = np.logspace(-3,5,nalpha)

# MSE for each alpha and fold value
mse = np.zeros((nalpha,nfold))
for ifold, ind in enumerate(kf.split(X)):
    
    
    # Get the training data in the split
    Itr,Its = ind
    X_tr = X[Itr,:]
    y_tr = y[Itr]
    X_ts = X[Its,:]
    y_ts = y[Its]
    
    # Compute the lasso path for the split
    for ia, a in enumerate(alphas):
        
        # Fit the model on the training data
        model.alpha = a
        model.fit(X_tr,y_tr)
        
        # Compute the prediction error on the test data
        y_ts_pred = model.predict(X_ts)
        mse[ia,ifold] = np.mean((y_ts_pred-y_ts)**2)

# Compute the mean and standard deviation over the different folds.
mse_mean = np.mean(mse,axis=1)
mse_std = np.std(mse,axis=1) / np.sqrt(nfold-1)

# Plot the mean MSE and the mean MSE + 1 std dev
plt.semilogx(alphas, mse_mean)
# plt.semilogx(alphas, mse_mean+mse_std)
# plt.legend(['Mean MSE', 'Mean MSE+1 SE'],loc='upper left')
plt.xlabel('alpha')
plt.ylabel('Test MSE')
plt.grid()
plt.show()