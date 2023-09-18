import pandas as pd
import scipy as sp
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mplot
from scipy import stats
from scipy.stats import poisson

# Problem 1A
gs = np.random.normal(size=10000, loc=7.25, scale=0.875)


# Problem 1B
matrix = np.array([[1.0, 0.6, -0.9], [0.6, 1.0, -0.5], [-0.9, -0.5, 1.0]])

APT = np.random.multivariate_normal(np.array([0, 0, 0]), matrix, size=10000)
corAPT = np.corrcoef(APT, rowvar=False)

sb.pairplot(pd.DataFrame(APT, columns=["ak", "pp", "ptime"]))
mplot.show()

mplot.hist(APT[:, 0])
mplot.show()


# Problem 1C
cdfAPT = stats.norm.cdf(APT[:, 0], loc=0, scale=1)
cdfAPT_for_cor = stats.norm.cdf(APT, loc=0, scale=1)
cdf_APT_for_plot = stats.norm.cdf(
    np.random.multivariate_normal(np.array([0, 0, 0]), matrix, size=10000)
)

mplot.hist(cdfAPT, bins=20)
mplot.show()

cor_Cdf_APT = np.corrcoef(cdfAPT_for_cor, rowvar=False)
print(cor_Cdf_APT)

sb.pairplot(pd.DataFrame(cdf_APT_for_plot, columns=["ak", "pp", "ptime"]))
mplot.show()

# Problem 1D
ak = poisson.ppf(APT[:, 0], 5)
mplot.hist(ak, bins=15)
mplot.show()

pp = poisson.ppf(APT[:, 1], 15)
mplot.hist(pp, bins=30)
mplot.show()

ptime = sp.stats.norm.ppf(APT[:, 2], loc=120, scale=30)
mplot.hist(ptime)
mplot.show()

mplot.hist(gs)
mplot.show()

# Problem 1E
df = pd.DataFrame({"ak": ak, "pp": pp, "ptime": ptime, "gs": gs})
sb.pairplot(pd.DataFrame(df))
mplot.show()
