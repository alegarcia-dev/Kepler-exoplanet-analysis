'''

    wrangle.py

    Description: This file contains functions used for both acquiring and 
        preparing the Kepler Exoplanet Archive data.

    Variables:

        None

    Functions:

        wrangle_kepler_explore()
        wrangle_kepler_modeling()
        wrangle_kepler()

'''

################################################################################

import pandas as pd

from acquire_kepler import AcquireKeplerData
from prepare import prepare_kepler_explore, prepare_kepler_modeling
from preprocessing import split_data

################################################################################

def wrangle_kepler_explore() -> pd.DataFrame:
    '''
        Acquire and prepare the kepler exoplanet data. Return the resulting 
        dataframe. This wrangle function is used in exploration.
    
        Returns
        -------
        DataFrame: The prepared kepler exoplanet data.
    '''

    return prepare_kepler_explore(AcquireKeplerData().get_data())

################################################################################

def wrangle_kepler_modeling() -> tuple[pd.DataFrame]:
    '''
        Acquire and prepare the kepler exoplanet data. Return the resulting 
        dataframe. This wrangle function is used in modeling.
    
        Returns
        -------
        DataFrame: The prepared kepler exoplanet data.
    '''

    return split_data(prepare_kepler_modeling(AcquireKeplerData().get_data()), stratify = 'disposition')

################################################################################

wrangle_kepler = wrangle_kepler_modeling