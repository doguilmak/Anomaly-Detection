# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 00:32:31 2021

@author: doguilmak

Anomaly Detection
In this study, 4 different anomaly detection methods are shown on a randomly 
generated dataset. Detailed explanations of these methods are available in the 
links in the comments.

"""
#%%
# Importing libraries

import matplotlib.pyplot as plt 
from sklearn.datasets import make_blobs
import numpy as np
from numpy import where
import time

#%%
# Creating dataset

start = time.time()
n_samples_1 = 1300

X, y = make_blobs(n_samples=n_samples_1, centers=[[4, 4]], cluster_std=0.45)

plt.figure(figsize=(12, 12))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Anomaly Detection')
plt.scatter(X[:, 0], X[:, 1], marker='.')
plt.show()

#%%
# 1. Local Outlier Factor
"""
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor
"""
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.03)
y_pred_lof=lof.fit_predict(X)

print("\nLocal Outlier Factor")
print(y_pred_lof)
print(lof.negative_outlier_factor_)

plt.figure(figsize=(12, 12))
plt.title("Local Outlier Factor (LOF)")
lofs_index = where(y_pred_lof==-1)
lofs_values=X[lofs_index]

plt.scatter(X[:, 0], X[:, 1], s=2.0)
plt.scatter(lofs_values[:, 0], lofs_values[:, 1], color='r')
plt.xlabel("prediction errors: %d" % (len(lofs_values[:, 0])))
plt.show()

n_outliers = len(lofs_values)
ground_truth = np.ones(len(X), dtype=int)
ground_truth[-n_outliers:] = -1

n_errors = (y_pred_lof != ground_truth).sum()
X_scores = lof.negative_outlier_factor_

plt.figure(figsize=(12, 12))
plt.title("Local Outlier Factor (LOF)")
plt.scatter(X[:, 0], X[:, 1], color="k", s=2.0, label="Data points")
# plot circles with radius proportional to the outlier scores
radius = (X_scores.max() - X_scores) / (X_scores.max() - X_scores.min())
plt.scatter(
    X[:, 0],
    X[:, 1],
    s=1000 * radius,
    edgecolors="r",
    facecolors="none",
    label="Outlier scores",
)

plt.xlim((2, 6))
plt.ylim((2, 6))
plt.show()

#%%
# 2. Elliptic Envelope
"""
https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope
"""
from sklearn.covariance import EllipticEnvelope

cov = EllipticEnvelope(random_state=0).fit(X)
y_pred_cov=cov.fit_predict(X)

print("\nElliptic Envelope")
print(cov.covariance_)
print(cov.location_)
print(y_pred_cov)

n_outliers = len((X[:, 0]))
ground_truth = np.ones(len(X), dtype=int)
ground_truth[n_outliers:] <= 0

plt.figure(figsize=(12, 12))
plt.title("Elliptic Envelope")
cov_index = where(y_pred_cov==-1)
cov_values=X[cov_index]

plt.scatter(X[:, 0], X[:, 1], s=2.0)
plt.scatter(cov_values[:, 0], cov_values[:, 1], color='r')
plt.xlabel("prediction errors: %d" % (len(cov_values[:, 0])))
plt.show()

#%%
# 3. One Class SVM
"""
https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM
"""
from sklearn.svm import OneClassSVM

ocSVM = OneClassSVM(gamma='auto').fit(X)
y_pred_ocSVM = ocSVM.predict(X)

print("\nOne Class SVM")
print(y_pred_ocSVM)
print(ocSVM.score_samples(X))

plt.figure(figsize=(12, 12))
plt.title("One Class SVM")
ocSVM_index = where(y_pred_ocSVM==-1)
ocSVM_values=X[ocSVM_index]

plt.scatter(X[:, 0], X[:, 1], s=2.0)
plt.scatter(ocSVM_values[:, 0], ocSVM_values[:, 1], color='r')
plt.xlabel("prediction errors: %d" % (len(ocSVM_values[:, 0])))
plt.show()
      
#%%
# 4. Isolation Forest
"""
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html
"""
from sklearn.ensemble import IsolationForest

isof = IsolationForest(random_state=0).fit(X)
y_pred_isof=isof.predict(X)

print("\nIsolation Forest")
print(y_pred_isof)
print(isof.decision_function(X))

plt.figure(figsize=(12, 12))
plt.title("Isolation Forest")
isof_index = where(y_pred_isof==-1)
isof_values=X[isof_index]

plt.scatter(X[:, 0], X[:, 1], s=2.0)
plt.scatter(isof_values[:, 0], isof_values[:, 1], color='r')
plt.xlabel("prediction errors: %d" % (len(isof_values[:, 0])))
plt.show()

end = time.time()
cal_time = end - start
print("\nProcess took {} seconds.".format(cal_time))
