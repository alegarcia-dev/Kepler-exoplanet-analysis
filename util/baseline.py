'''

    baseline.py

    Description: This file provides functions for easily establishing baseline 
        models in machine learning problems.

    Variables:

        None

    Functions:

        establish_regression_baseline(target)
        establish_classification_baseline(target)

'''

import pandas as pd

from sklearn.metrics import mean_squared_error

################################################################################

def establish_regression_baseline(target: pd.DataFrame) -> pd.Series:
    '''
        Determine whether to use the mean of the target or the median of the 
        target as the baseline model for a regression problem.
    
        Parameters
        ----------
        target: DataFrame
            The target variable for a regression problem.
    
        Returns
        -------
        Series: A pandas Series containing the best performer between the 
            median and mean of the target variable.
    '''

    baseline = pd.DataFrame({
        'median' : target.median(),
        'mean' : target.mean()
    }, index = target.index)

    median_rmse = mean_squared_error(target, baseline["median"], squared = False)
    mean_rmse = mean_squared_error(target, baseline["mean"], squared = False)

    return baseline['median'] if median_rmse < mean_rmse else baseline['mean']

################################################################################

def establish_classification_baseline(target: pd.DataFrame) -> pd.Series:
    '''
        Returns a pandas series containing the most common value in the target 
        variable that is of the same size as the provided target. This series 
        serves as the baseline model to which to compare any machine learning 
        models.

        Parameters
        ----------
        target: DataFrame
            A pandas series containing the target variable for a machine 
            learning project.

        Returns
        -------
        Series: A pandas series with the same size as target filled with the 
            most common value in target.
    '''

    most_common_value = target.mode()[0]
    return pd.Series(most_common_value, index = target.index)