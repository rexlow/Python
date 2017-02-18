def Accuracy(features_train, labels_train, features_test, labels_test):
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train, labels_train)

    # use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)

    # calculate accuracy with this module
    # general formula as follows
    # accuracy = no of points classified correctly / all points
    from sklearn.metrics import accuracy_score
    return accuracy_score(pred, labels_test)
