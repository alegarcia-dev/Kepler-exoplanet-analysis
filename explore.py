'''

    explore.py

    Description: This file contains functions used for producing visualizations 
        conducting statistical tests in the kepler exoplanet final report.

    Variables:

        None

    Functions:

        plot_orbital_period(df)
        plot_planetary_radius(df)
        plot_transit_depth(df)
        plot_transit_duration(df)
        two_sample_ttest(sample1, sample2, feature, alternative = 'two-sided', alpha = 0.05)

'''

################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from preprocessing import remove_outliers

################################################################################

def plot_orbital_period(df: pd.DataFrame) -> None:
    plt.figure(figsize = (14, 4))
    
    sns.barplot(
        data = remove_outliers(df, 3.0, ['orbital_period']),
        x = 'disposition',
        y = 'orbital_period',
        ci = None
    )

    plt.title('Confirmed exoplanets tend to have longer orbital periods.')

    plt.xlabel('Disposition')
    plt.ylabel('Orbital Period (Days)')

    plt.show()

################################################################################

def plot_planetary_radius(df: pd.DataFrame) -> None:
    plt.figure(figsize = (14, 4))
    
    sns.barplot(
        data = df,
        x = 'disposition',
        y = 'planetary_radius',
        ci = None
    )

    plt.title('False positives have significantly greater planetary radius on average.')

    plt.xlabel('Disposition')
    plt.ylabel('Planetary Radius (Earth radii)')

    plt.show()

################################################################################

def plot_transit_depth(df: pd.DataFrame) -> None:
    plt.figure(figsize = (14, 4))
    
    sns.barplot(
        data = df,
        x = 'disposition',
        y = 'transit_depth',
        ci = None
    )

    plt.title('False positives have significantly greater transit depth on average.')

    plt.xlabel('Disposition')
    plt.ylabel('Transit Depth (parts per million)')

    plt.show()

################################################################################

def plot_transit_duration(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(ncols = 2, nrows = 1, figsize = (14, 4))

    sns.histplot(
        data = remove_outliers(df, 1.5, ['transit_duration']),
        x = 'transit_duration',
        hue = 'disposition',
        bins = 20,
        ax = ax[0]
    )

    ax[0].set(
        title = 'There is a similar distribution of transit duration for non-outliers.',
        xlabel = 'Transit Duration'
    )

    sns.histplot(
        data = df[df.transit_duration >= 20],
        x = 'transit_duration',
        hue = 'disposition',
        bins = 20,
        ax = ax[1]
    )

    ax[1].set(
        title = 'Outliers are almost exclusively false positives.',
        xlabel = 'Transit Duration'
    )

    plt.show()

################################################################################

def two_sample_ttest(sample1: pd.DataFrame, sample2: pd.DataFrame, feature: str, alternative: str = 'two-sided', alpha: float = 0.05) -> None:
    _, p = stats.ttest_ind(sample1[feature], sample2[feature], equal_var = False, alternative = alternative)

    if p < alpha:
        print('Reject H0')
    else:
        print('Fail to reject H0')