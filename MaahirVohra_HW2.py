import matplotlib as mpl
import pandas as pd
import scipy as sp
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mplot
from scipy import stats
from scipy.stats import poisson
import random
import sys
assert sys.version_info >= (3, 7)
from packaging import version
import sklearn
from pathlib import Path
from sklearn.preprocessing import add_dummy_feature
assert version.parse(sklearn.__version__) >= version.parse("1.0.1")

# Load the dataset
dataURL = r"/Users/maahirvohra/Desktop/Code/CS370/imports-85.csv"
data = pd.read_csv(dataURL)

# Extract the relevant columns (curb weight, engine size, and MPG)
X = data[['curb-weight', 'engine-size']].values
y = data['city-mpg'].values

# Add a column of ones to the feature matrix for the bias term
X_b = np.c_[np.ones((len(X), 1)), X]

# Set up hyperparameters
nEpochs = 50
t0, t1 = 5, 50  # learning schedule hyperparameters
alph = 0.001  # Regularization strength (L2 regularization)

def learningSchedule(t):
    return t0 / (t + t0)

np.random.seed(42)
theta = np.random.randn(3, 1)  # random initialization

nShown = 21 # Number of lines to show in the plot (for visualization)
thetaPathSGD = []  # To store the path of theta for plotting

mplot.figure(figsize=(7, 4))  # Figure size for plotting

for epoch in range(nEpochs):
    for i in range(len(X)):

        if epoch == 0 and i < nShown:
            yPredict = X_b @ theta
            color = mpl.colors.rgb2hex(mplot.cm.OrRd(i / nShown + 0.15))
            mplot.plot(X_b, yPredict, color=color)


        randIndex = np.random.randint(len(X))
        x1 = X_b[randIndex:randIndex + 1]
        yi = y[randIndex:randIndex + 1]
        gradients = 2 * x1.T @ (x1 @ theta - yi) + 2 * alph * theta  # Include L2 regularization term
        eta = learningSchedule(epoch * len(X) + i)
        theta = theta - eta * gradients
        thetaPathSGD.append(theta) 

        # Plot the data points
mplot.plot(X, y, "b.")
mplot.xlabel("Curb Weight and Engine Size")
mplot.ylabel("MPG", rotation=0)
mplot.axis([0, max(X[:, 0]), min(y), max(y)])
mplot.grid()
mplot.show()

print("Asked professor for help on graphing the normal distribution line and he said 'I dont know the data'. \nI've tried for the past 3 days to make it work")
