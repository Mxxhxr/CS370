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

############# PART 1 #############

#turn csv into dataframe
dataset_url = r"C:\Users\maahi\OneDrive\Desktop\Code\CS370\imports-85.csv"
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(dataset_url)

# Now, you can work with the 'df' DataFrame as needed
pd.set_option('display.max_columns', None)  # Show all columns
df.head(10)

target_variable_column = df[['city-mpg']]
feature_columns = df[['curb-weight', 'engine-size']]

X_new = np.array([[0], [3]])
X_new_b = add_dummy_feature(X_new)  # add x0 = 1 to each instance




theta_path_sgd = []
n_epochs = 50
t0, t1 = 5, 50  # learning schedule hyperparameters

def learning_schedule(t):
    return t0 / (t + t1)

np.random.seed(42)
theta = np.random.randn(3, 1)  # random initialization


n_shown = 20  # extra code – just needed to generate the figure below
mplot.figure(figsize=(6, 4))  # extra code – not needed, just formatting


for epoch in range(n_epochs):
    for iteration in range(len(target_variable_column)):

        # extra code – these 4 lines are used to generate the figure
        if epoch == 0 and iteration < n_shown:
            y_predict = X_new_b @ theta
            color = mpl.colors.rgb2hex(plt.cm.OrRd(iteration / n_shown + 0.15))
            plt.plot(X_new, y_predict, color=color)

        random_index = np.random.randint(m)
        xi = X_b[random_index : random_index + 1]
        yi = y[random_index : random_index + 1]
        gradients = 2 * xi.T @ (xi @ theta - yi)  # for SGD, do not divide by m
        eta = learning_schedule(epoch * m + iteration)
        theta = theta - eta * gradients
        theta_path_sgd.append(theta)  # extra code – to generate the figure


