import numpy as np
from sklearn.naive_bayes import GaussianNB

# features
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

# labels
Y = Y = np.array([1, 1, 1, 2, 2, 2])

# classifiers
clf = GaussianNB()
clf.fit(X, Y) #train
GaussianNB(priors=None)
print(clf.predict([[-0.8, -1]]))

#partial fit
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
GaussianNB(priors=None)
print(clf_pf.predict([[-0.8, -1]]))
