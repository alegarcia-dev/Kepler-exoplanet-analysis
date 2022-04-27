'''

    evaluate.py

    Description: This file contains functions that are used for evaluating 
        the performance of machine learning models.

    Variables:

        None

    Functions:

        evaluate()
        append_results(index, target, actual, prediction, evaluate_results = None)

'''

################################################################################

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score

################################################################################

def evaluate(target: pd.Series, prediction: pd.Series, positive_label: str, prefix: str = ''):
    return {
        prefix + 'accuracy' : accuracy_score(target, prediction),
        prefix + 'recall' : recall_score(target, prediction, pos_label = positive_label, zero_division = 0),
        prefix + 'precision' : precision_score(target, prediction, pos_label = positive_label, zero_division = 0)
    }

################################################################################

def append_results(index: str, results: dict, evaluate_df: pd.DataFrame = None) -> pd.DataFrame:
    '''
        Append the evaluation results to the evaluate_df or if an evaluate_df 
        is not provided, create one and append the results.
    
        Parameters
        ----------
        index: str
            The index to assign to the results entry provided. A string provides 
            a more descriptive index, but any valid dataframe index is acceptable.

        results: dict[str : float]
            The results of the model evaluation in the form of a dictionary with 
            the metric as the key and the result as a float.

        evaluate_df: DataFrame, optional
            The evaluation dataframe to append the results to. Default is to 
            create a new dataframe.
    
        Returns
        -------
        DataFrame: The evaluate_df with the results appended.
    '''

    if evaluate_df is None:
        evaluate_df = pd.DataFrame()

    df = pd.DataFrame(results, index = [index])
    
    return evaluate_df.append(df)