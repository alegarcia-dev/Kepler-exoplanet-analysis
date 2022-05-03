'''

    model.py

    Description: This file contains functions that are used for modeling in the 
        kepler exoplanet project.

    Variables:

        None

    Functions:

        establish_baseline(train, validate, target)

    Classes:

        Model(model, train, features, target)
        establish_baseline(train, validate, target)
        create_and_train_models(train, target, random_seed = 24)
        evaluate_model(model, name, train, validate, target, eval_df)

'''

################################################################################

import pandas as pd

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC

from baseline import establish_classification_baseline
from evaluate import *

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

################################################################################

def establish_baseline(train: pd.DataFrame, validate: pd.DataFrame, target: str) -> pd.DataFrame:
    results = {
        **evaluate(train[target], establish_classification_baseline(train[target]), 'CONFIRMED', prefix = 'train_'),
        **evaluate(validate[target], establish_classification_baseline(validate[target]), 'CONFIRMED', prefix = 'validate_')
    }

    return append_results('Baseline', results)

################################################################################

def create_and_train_models(train: pd.DataFrame, target: str, random_seed: int = 24) -> dict:
    model_objects = [
        DecisionTreeClassifier(max_depth = 3, random_state = random_seed),
        GradientBoostingClassifier(random_state = random_seed),
        GradientBoostingClassifier(loss='exponential', n_estimators=300, random_state=24),
        GradientBoostingClassifier(loss='exponential', n_estimators=300, random_state=24)
    ]

    names = [
        'Decision Tree',
        'Gradient Boosting Classifier',
        'Gradient Boosting Variant 1',
        'Gradient Boosting Variant 2'
    ]

    features = [
        'planetary_radius',
        'orbital_period',
        'normalized_depth',
        'transit_depth',
        'transit_duration'
    ]

    end_index = [2, 2, 2, 5]

    models = {}

    for index, model in enumerate(model_objects):
        models[names[index]] = Model(
            model,
            train,
            features[0 : end_index[index]],
            target
        )

    return models

################################################################################

def evaluate_model(model, name, train: pd.DataFrame, validate: pd.DataFrame, target: str, eval_df: pd.DataFrame) -> pd.DataFrame:
    return append_results(
        name,
        {
            **evaluate(train[target], model.make_predictions(train), 'CONFIRMED', prefix = 'train_'),
            **evaluate(validate[target], model.make_predictions(validate), 'CONFIRMED', prefix = 'validate_')
        },
        eval_df
    )