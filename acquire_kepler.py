'''

    acquire_kepler.py

    Description: This file contains a class that can be used for acquiring the 
        Kepler exoplanet search results dataset from kaggle. Use the get_data 
        function to acquire the data.

        Example:
            df = AcquireKeplerData("file_name.csv").get_data()

    Class:

        AcquireKeplerData

    Class Fields:

        None

    Class Methods:

        read_from_source(self)

    Inherited Fields:
        
        file_name

    Inherited Methods:

        __init__(self, file_name, database_name, sql)
        get_data(self, use_cache = True, cache_data = True)

'''

################################################################################

import os
import pandas as pd

################################################################################

class AcquireKeplerData(Acquire):

    ################################################################################

    def read_from_source(self):
        '''
            Acquire the Kepler exoplanet search results data with the Kaggle API.
            If the Kaggle API is not installed an exception is raised.

            This function will remove all files downloaded from Kaggle. Any cacheing
            is done by the Acquire class in the get_data method.
        
            Returns
            -------
            DataFrame: A pandas dataframe containing the Kepler data.
        '''

        shell_output = os.system('kaggle datasets download nasa/kepler-exoplanet-search-results -f cumulative.csv')
        if shell_output != 0:
            raise SystemError('''
                An error occurred when running "kaggle datasets download".
                You must either follow the instructions for installing the Kaggle API
                here https://github.com/Kaggle/kaggle-api or manually download the 
                data from here https://exoplanetarchive.ipac.caltech.edu/docs/data.html
            ''')
        
        os.system('unzip cumulative.csv.zip')
        os.system('rm cumulative.csv.zip')
        df = pd.read_csv('cumulative.csv')
        os.system('rm cumulative.csv')
        
        return df