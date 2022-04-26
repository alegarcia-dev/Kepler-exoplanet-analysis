'''

    wrangle.py

    Description: This file contains functions used for both acquiring and 
        preparing the Kepler Exoplanet Archive data.

    Variables:

        None

    Functions:

        wrangle_kepler_explore()

'''

################################################################################

import pandas as pd

from acquire_kepler import AcquireKeplerData
from prepare import prepare_kepler

################################################################################

def wrangle_kepler_explore() -> pd.DataFrame:
    '''
        Acquire and prepare the kepler exoplanet data. Return the resulting 
        dataframe.
    
        Returns
        -------
        DataFrame: The prepared kepler exoplanet data.
    '''

    return prepare_kepler(AcquireKeplerData('kepler.csv').get_data())