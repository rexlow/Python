import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
# %pylab inline
import matplotlib.pyplot as plt

raw_data = pd.read_csv("linear.csv")
raw_data.head(3)

# preprocess the data to remove any points with a missing y value
filtered_data = raw_data[~np.isnan(raw_data["y"])]
filtered_data.head(3)

npMatrix = np.matrix(filtered_data)
X, Y = npMatrix[:,0], npMatrix[:,1]
mdl = LinearRegression().fit(X, Y)
m = mdl.coef_[0]
b = mdl.intercept_
print "formula: y = {0}x + {1}".format(m, b) # following slope intercept form
