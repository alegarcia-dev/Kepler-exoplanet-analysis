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
        create_cache_file(self, df, cache_data = True, verbose = False)

    Inherited Fields:
        
        file_name

    Inherited Methods:

        __init__(self, file_name)
        get_data(self, use_cache = True, cache_data = True)

'''

################################################################################

import os
import pandas as pd

################################################################################

class AcquireKeplerData(Acquire):

    ################################################################################

    def read_from_source(self) -> pd.DataFrame:
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
        
        return df

    ################################################################################

    def create_cache_file(self, df: pd.DataFrame, cache_data: bool = True, verbose: bool = True) -> None:
        '''
            Cache the dataframe in a .csv file if cache_data is True.
        
            Parameters
            ----------
            df: DataFrame
                A pandas dataframe with which to cache in a .csv file.

            cache_data: bool, optional
                If True the dataframe will be cached in a .csv file.

            verbose: bool, optional
                If True details about the steps being taken by this function 
                will be printed to the console.
        '''

        if cache_data:
            if verbose: print('Cacheing data.')
            os.system(f'mv cumulative.csv {self.file_name}')
        else:
            if verbose: print('Data not cached.')
            os.system('rm cumulative.csv')