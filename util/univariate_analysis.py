'''

    univariate_analysis.py

    Description: This file contains useful functions for performing univariate
        analysis, which can be used pre-split in the preparation phase of the
        data science pipeline.

    Variables:

        None

    Functions:

        get_hist(df, columns)
        get_box(df, columns)
        _create_sub_plots(num_columns)
        plot_single_variable(df, feature, title = '', histplot_bins = 50)
        summarize_column_nulls(df)
        summarize_row_nulls(df)

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

################################################################################

def get_hist(
    df: pd.DataFrame,
    columns: list[str],
    *,
    bins: int = 20,
    label_rotation: int = 30,
    figure_width: int = 14,
    figure_height: int = 4
) -> None:
    '''
        Gets histographs of acquired continuous variables.
        
        Parameters
        ----------
        df: DataFrame
            A pandas dataframe from which we will visualize the univariate 
            distributions of features.

        columns: list[str]
            A list of the columns we would like to visualize.

        bins: int, keyword optional
            The number of bins to use in each histogram. Default is 20.

        label_rotation: int, keyword optional
            The number of degrees to rotate the tick labels. Default is 30.

        figure_width: int, keyword optional
            The width of the figure. Default is 14.

        figure_height: int, keyword optional
            The height of each individual plot. Default is 4.
    '''

    fig, ax = plt.subplots(ncols = 1, nrows = len(columns), figsize = (figure_width, figure_height * len(columns)))

    for index, column in enumerate(columns):
        sns.histplot(
            data = df[column],
            bins = bins,
            ax = ax[index]
        )

        # Rotate the tick labels in case there are some lengthy tick labels.
        ax[index].tick_params(labelrotation = label_rotation)

        # Title with column name.
        ax[index].set_title(column)

        # turn off scientific notation
        plt.ticklabel_format(useOffset=False)

        plt.grid(False)

    plt.tight_layout()
    plt.show()

################################################################################

def get_box(
    df: pd.DataFrame,
    columns: list[str],
    *,
    bins: int = 20,
    label_rotation: int = 30,
    figure_width: int = 14,
    figure_height: int = 4
) -> None:
    '''
        Gets boxplots of acquired continuous variables.
        
        Parameters
        ----------
        df: DataFrame
            A pandas dataframe from which we will visualize the univariate 
            distributions of features.

        columns: list[str]
            A list of the columns we would like to visualize.

        bins: int, keyword optional
            The number of bins to use in each histogram. Default is 20.

        label_rotation: int, keyword optional
            The number of degrees to rotate the tick labels. Default is 30.

        figure_width: int, keyword optional
            The width of the figure. Default is 14.

        figure_height: int, keyword optional
            The height of each individual plot. Default is 4.
    '''

    fig, ax = plt.subplots(ncols = 1, nrows = len(columns), figsize = (figure_width, figure_height * len(columns)))

    for index, column in enumerate(columns):
        sns.boxplot(
            data = df,
            x = column,
            ax = ax[index]
        )

        # Rotate the tick labels in case there are some lengthy tick labels.
        ax[index].tick_params(labelrotation = label_rotation)

        # Title with column name.
        ax[index].set_title(column)

        # turn off scientific notation
        plt.ticklabel_format(useOffset=False)

        plt.grid(False)
        
    plt.tight_layout()
    plt.show()

################################################################################

def plot_single_variable(df: pd.DataFrame, feature: str, title: str = '', bins: int = 20):
    '''
        Create a histogram and boxplot for a single variable.
    
        Parameters
        ----------
        df: DataFrame
            A dataframe with data that needs to be plotted.

        feature: str
            The name of the variable to plot.

        title: str, optional
            An optional title to include with the plots.

        bins: int, optional
            The number of bins to use for the histogram. Default is 20.
    '''

    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (14, 4))
    fig.suptitle(title)

    sns.histplot(df[feature], bins = bins, ax = ax[0])
    sns.boxplot(data = df, x = feature, ax = ax[1])

    plt.show()

################################################################################

def summarize_column_nulls(df: pd.DataFrame) -> pd.DataFrame:
    '''
        Returns a dataframe with a summary of all column-wise missing values 
        in df.
    
        Parameters
        ----------
        df: DataFrame
            A pandas dataframe with which to summarize missing values.
    
        Returns
        -------
        DataFrame: A pandas dataframe containing the number of missing values 
            and percentage of values missing for each column in df.
    '''

    return pd.concat([
        df.isnull().sum().rename('rows_missing'),
        df.isnull().mean().rename('percent_missing')
    ], axis = 1)

################################################################################

def summarize_row_nulls(df: pd.DataFrame) -> pd.DataFrame:
    '''
        Returns a dataframe with a summary of all row-wise missing values 
        in df.
    
        Parameters
        ----------
        df: DataFrame
            A pandas dataframe with which to summarize missing values.
    
        Returns
        -------
        DataFrame: A pandas dataframe containing the number of missing values 
            and percentage of values missing for each row in df.
    '''

    return pd.concat([
        df.isnull().sum(axis = 1).rename('columns_missing'),
        df.isnull().mean(axis = 1).rename('percent_missing')
    ], axis = 1).value_counts().sort_index()