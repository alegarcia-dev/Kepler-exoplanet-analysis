'''

    model.py

    Description: This file contains functions that are used for modeling in the 
        kepler exoplanet project.

    Variables:

        None

    Functions:

        Function

    Classes:

        Model(model, train, features, target)

'''

################################################################################

import pandas as pd

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC

################################################################################

class Model:

    ################################################################################

    def __init__(self, model, train, features, target):
        self.model = model
        self.features = features
        self.target = target

        self.model.fit(train[self.features], train[self.target])

    ################################################################################

    def make_predictions(self, df):
        return self.model.predict(df[self.features])