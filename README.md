# Predicting Kepler Exoplanet Archive Disposition

This repository contains all files, and ipython notebooks, used in the Kepler exoplanet project. A full outline of all the files with descriptions can be found below.

## Repository Format

<details>
<summary><i>Click to expand</i></summary>

- README.md: Contains a full outline of the project, information regarding the format of the repository, and instructions for reproducing the results.
- kepler_exoplanet_report.ipynb: The final report containing a high level overview of the project including key takeaways, final results, and a recommendations.
- notebooks: A directory containing all working notebooks for each phase of the pipeline.

</details>

___

## Table of Contents

1. [Project Summary](#project-summary)
2. [Project Planning](#project-planning)
3. [Data Dictionary](#data-dictionary)
4. [Outline of Project Plan](#outline-of-project-plan)
    1. [Data Acquisition](#data-acquisition)
    2. [Data Preparation](#data-preparation)
    3. [Exploratory Analysis](#exploratory-analysis)
    4. [Modeling](#modeling)
5. [Conclusion](#conclusion)
6. [Recreate This Project](#instructions-for-recreating-this-project)

___

## Project Summary

Data from the NASA Exoplanet Archive was used to determine the attributes that distinguish confirmed exoplanets from false positives, or objects identified as candidate exoplanets that are determined to not be exoplanets after further analysis. A classification model that is robust to newly obtained observations was produced and obtained 90% accuracy on unseen data.

___

## Project Planning

<details><summary><i>Click to expand</i></summary>

### Project Goals

Identify drivers of the exoplanet archive disposition to determine which attributes are most likely to be predictive of the dispositions of confirmed exoplanet or false positive.

### Project Description

The Kepler Space Observatory is a NASA-built telescope dedicated to searching for exoplanets in star systems besides our own, with the ultimate goal of possibly finding other habitable planets. The Kepler Space Observatory is retired as of October 30, 2018, but all the data it collected can be accessed from the NASA Exoplanet Archive [here](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative), or from Kaggle [here](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results). Observations in the Kepler Object of Interest table were made using the transit method for identifying exoplanets in other star systems. The transit method involves measuring the light intensity of a host star over time and looking for periodic dips in light intensity which signify an object eclipsing the host star, which could potentially indicate the presence of an exoplanet.

Identifying exoplanets can be a time consuming process particularly for planets with long orbital periods, such as planets that like the Earth may take upwards of a year to orbit their host star. With that in mind when candidate exoplanets are identified being able to prioritize the candidates that will most likely be confirmed can help to further the goal of identifying exoplanets. So we would like to determine which attributes are most indicative of a confirmed exoplanet disposition and similarly which attributes are most indicative of a false positive disposition. Finally, once these attributes are determined they will be used to produce a reusable machine learning model that can help predict which exoplanet candidates are most likely to be confirmed.

As a data scientist with an interest in astronomy I aim to provide a means for determining which objects of interest will be most likely to result in newly discovered exoplanets. This way time is not lost observing objects that may end up not being exoplanets.

### What Should The End Result Be?

The goal of this project (in regards to final deliverables) is to provide reproducible and reusable work. The deliverables are as follows:

- A reproducible ipython notebook providing an overview of the project, all steps taken, and key takeaways.
- .py files that can be used to reproduce all steps taken.

### Initial Questions

We are trying to find drivers of the exoplanet archive disposition so we want to identify the features in the data that provide the most meaningful information in regards to whether an object of interest is likely to be a confirmed exoplanet or a false positive. However, with that in mind we should also be sure to not use features that leak information about the target as this would defeat the purpose. So we aim to answer the following questions:

- What features are most indicative of a confirmed exoplanet disposition?
- What features are most indicative of a false positive disposition?
- Which features leak information about the target and should be removed in preparation?
- Can the features that are predictive of the target be narrowed down so as to provide an easily reusable modeling solution?

### Who is The Audience?

This project is intended for a general audience so technical language is kept to a minimum. For those interested, technical details can be found in the working notebooks in the notebooks directory, or within the .py files.

</details>

___

## Data Dictionary

<details><summary><i>Click to expand</i></summary>

Only the features that are mentioned most frequently are defined in this dictionary. For the full data dictionary and more details refer to this [link](https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html).

| Variable              | Meaning      |
| --------------------- | ------------ |
| disposition / koi_disposition | The category of this object of interest from the exoplanet archive. |
| transit_depth / koi_depth | The fraction of stellar flux lost at the minimum of planetary transit (parts per million). |
| planetary_radius / koi_prad | The radius of the planet. Planetary radius is the product of the planet star radius ratio and the stellar radius. |
| temperature / koi_teq | Approximation for the temperature of the planet. |
| normalized_depth / koi_model_snr | Transit depth normalized by the mean uncertainty in the flux during the transits. |
| orbital_period / koi_period | The interval between consecutive planetary transits. |
| transit_duration / koi_duration | The duration of the observed transits. Duration is measured from first contact between the planet and star until last contact. |
| koi_pdisposition      | The pipeline flag that designates the most probable physical explanation of the object of interest. |
| koi_score             | A value between 0 and 1 that indicates the confidence in the object of interest disposition. |
| koi_fpflag_nt         | Not transit-like flag. An object of interest whose light curve is not consistent with that of a transiting planet. |
| koi_fpflag_ss         | Stellar eclipse flag. An object of interest that is observed to have a significant secondary event, transit shape, or out-of-eclipse variability, which indicates that the transit-like event is most likely caused by an eclipsing binary. |
| koi_fpflag_co         | Centroid offset flag. The source of the signal is from a nearby star, as inferred by measuring the centroid location of the image both in and out of transit. |
| koi_fpflag_ec         | Ephemeris match indicates contamination flag. The object of interest shares the same period and epoch as another object and is judged to be the result of flux contamination in the aperture or electronic crosstalk. |

</details>

___

## Outline of Project Plan

The following outlines the process taken through the Data Science Pipeline to complete this project.
<br>
Plan &#8594; Acquire &#8594; Prepare &#8594; Explore &#8594; Model &#8594; Deliver

---
### Data Acquisition

**Acquisition Files:**
- wrangle.ipynb, contains a section on data acquisition that covers all the steps taken in the data acquisition phase.
- acquire_kepler.py, contains the code needed to download the data from the source and has code used for cacheing the data.
- acquire.py, contains a parent class used by the acquire_kepler.py file.

**Steps Taken:**
- The data is acquired from Kaggle [here](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results), using the Kaggle API. This requires an API key. Alternatively, the .csv file can be downloaded manually from Kaggle.
- The data can also be acquired from the NASA Exoplanet Archive [here](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative), using the NASA Exoplanet Archive API. This does not require an API key, but a key can be obtained. Alternatively, the .csv file can be downloaded from the NASA Exoplanet Archive site. The site states that the organization is in the process of updating the API to a different format so the code used in this project may not work in the future. It's better to rely on the Kaggle API.
- The code that reads the data from the source will first attempt to utilize the Kaggle API before attempting to use the NASA API.
- All acquisition code is abstracted in the acquire_kepler.py and acquire.py files for reusability. By default the downloaded data will be cached in a kepler.csv file unless otherwise specified or if a different file name is provided.

### Data Preparation

**Preparation Files:**
- wrangle.ipynb, contains a section on data preparation that covers all the steps taken in the data preparation phase.
- wrangle.py, contains functions that can be used to both acquire and prepare the data (for various phases) in one step.
- prepare.py, contains functions that are used in the preparation of the Kepler exoplanet data.
- preprocessing.py, contains functions that are used for data splitting and scaling for the exploration and modeling phases.

**Steps Taken:**
- The raw data contains some missing values. A few columns are nearly empty upon loading the raw data. Columns with a large percentage of missing values are dropped. Then any rows still missing values are dropped. This leaves 94% of the original columns and 82% of the observations remaining.
- The target variable (disposition / koi_disposition) has three unique values: FALSE POSITIVE, CONFIRMED, and CANDIDATE. Any observations with a disposition of CANDIDATE are removed since these observations do not fit into the scope of this project. This leaves 63% of the original observations remaining.
- A few columns (such as id columns) can be determined at this stage to not be useful and are dropped.
- A few of the columns are renamed for readability. This renaming mostly only applies to the modeling phase and final report. Going into exploration only the target is renamed so as not to lose time renaming columns that won't be used beyond exploration. There were a lot of columns.
- All preparation code is abstracted in the prepare.py and wrangle.py files for reusability.

### Exploratory Analysis

**Exploratory Analysis Files:**
- explore.ipynb, covers all the steps taken in the exploratory analysis phase.
- explore.py, contains functions that are used for producing visualizations and conducting statistical tests in the final report.
- univariate_analysis.py, contains functions that are used for performing univariate analysis in the explore notebook.
- bivariate_analysis.py, contains functions that are used for performing bivariate analysis in the explore notebook.

**Steps Taken:**
- The data is acquired, prepared, and split since it is the intention to build a machine learning model.
- Univariate analysis is conducted to visualize the distributions of all the variables and identify which variables have outliers, which possibly leak information about the target, and which can be ignored due to lack of usefulness.
- Bivariate analysis is conducted to visualize how a few variables chosen after univariate analysis interact with the target variable. Here a few more features are identified as leaking information about the target and the best features for predicting the target are chosen.
- Statistical tests are performed on the chosen features to determine if there is significant differences in these features between the two samples, false positives and confirmed exoplanets.
- Multivariate analysis is conducted to identify how various features interact with each other. Nothing immediately useful is identified in this section so no insights are gained here.
- All results of exploration are gathered and formalized. The following features are identified as most pertinent to the project goals:
    - transit_depth
    - planetary_radius
    - temperature
    - normalized_depth
    - orbital_period
    - transit_duration

### Modeling

**Modeling Files:**
- model.ipynb, covers all the steps taken in the modeling phase.
- model.py, contains functions used for producing machine learning models in the model notebook and final report.
- evaluate.py, contains functions used for evaluating the performance of machine learning models.
- baseline.py, contains functions used for establishing a baseline model.

**Steps Taken:**
- The data is acquired, prepared, and split using the wrangle module produced in the preparation phase.
- The data is scaled since some of the features have very wide ranges of values.
- The models are to be evaluated using the accuracy score, with precision as a tie breaker if needed. The reason for using accuracy is that our target is fairly evenly split and we are equally interested in accuractely predicting false positives and confirmed exoplanets, because accurate predictions in both cases will help to guide priorities for further observations. Precision is used as a secondary evaluation metric, because in the case that we cannot achieve high accuracy we want to prioritize correctly identifying confirmed exoplanets, where a confirmed disposition is the positive label, since these observations will be given priority for further analysis to determine the true disposition.
- A baseline model is established with which to compare our models to. This will provide a minimally viable product that uses the simplest approach to achieve accurate results. In this case the most frequent value in the target variable is the only predition made by the baseline model.
- A feature selection algorithm is used to rank the importance of the features chosen in exploration so that when adding more features to our models we can add them in the order they are ranked.
- Models using various machine learning algorithms are created using a subset of the chosen features. The algorithm with the best overall performance is chosen to move forward.
- Various combinations of hyper-parameters are used with the best algorithm to produce more models. The model with the best performance is chosen to move forward.
- Using the best algorithm with the best combination of hyper-parameters several more models are produced with added features.
- The best model is chosen and evaluated on the unseen test dataset.

___

## Conclusion

- Much of the raw data consists of observations that have a disposition of candidate exoplanet. These observations cannot be used since we are only interested in dispositions of false positive or confirmed exoplanet. Additionally, a lot of null values exist in the raw data and needed to be removed.
- A few features in the data leak information about the target variable and should therefore not be used in modeling. Some research and analysis was conducted to show that these features would not be available to us given new observations either way so using these features in our model would ultimately result in a model that doesn't work with new observations.
- Exploratory analysis revealed a few features were useful for distinguishing false positive observations from confirmed exoplanet observations. Namely, planetary radius, orbital period, normalized depth, transit depth, transit duration, and planetary approximate temperature. Statistical tests confirmed that the difference in each of these features between false positives and confirmed exoplanets was significant.
- A large variety of machine learning models were produced using various algorithms and hyper-parameters. It was shown that using the features identified in exploration could produce a highly accurate model for predicting exoplanet disposition. A Gradient Boosting Classifier produced the best results and was able to predict exoplanet archive disposition on unseen data with nearly 90% accuracy.

___

## Instructions For Recreating This Project

1. Clone this repository into your local machine using the following command:
```bash
git clone git@github.com:alegarcia-dev/kepler-exoplanet-analysis.git
```
2. You will need Pandas, Numpy, Matplotlib, Seaborn, SKLearn, and the Kaggle API installed on your machine.
    - If you do not have the Kaggle API installed follow these [instructions](https://github.com/Kaggle/kaggle-api) to install it.
3. Now you can start a Jupyter Notebook session and execute the code blocks in the kepler_exoplanet_report.ipynb notebook.

[Back to top](#exploring-kepler-exoplanet-data)