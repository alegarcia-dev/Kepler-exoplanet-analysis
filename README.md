# Exploring Kepler Exoplanet Data

This repository contains all files, and ipython notebooks, used in the Kepler exoplanet project. A full outline of all the files with descriptions can be found below.

## Repository Format

<details>
<summary><i>Click to expand</i></summary>

- README.md: Contains a full outline of the project, information regarding the format of the repository, and instructions for reproducing the results.

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

<i>pending</i>

___

## Project Planning

<details><summary><i>Click to expand</i></summary>

### Project Goals

Identify drivers of the exoplanet archive disposition to determine which attributes are most likely to be predictive of the dispositions of confirmed exoplanet or false positive.

### Project Description

The Kepler Space Observatory is a NASA-built telescope dedicated to searching for exoplanets in star systems besides our own, with the ultimate goal of possibly finding other habitable planets. The Kepler Space Observatory is retired as of October 30, 2018, but all the data it collected can be accessed from the NASA Exoplanet Archive [here](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative), or from Kaggle [here](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results). Observations in the Kepler Object of Interest table were made using the transit method for identifying exoplanets in other star systems. The transit method involves measuring the light intensity of a host star over time and looking for periodic dips in light intensity which signify an object eclipsing the host star, which could potentially indicate the presence of an exoplanet.

Identifying exoplanets can be a time consuming process particularly for planets with long orbital periods, that is planets that like the Earth may take upwards of a year to orbit their host star. With that in mind when candidate exoplanets are identified being able to prioritize the candidates that will most likely be confirmed can help to further the goal of identifying exoplanets. So we would like to determine which attributes are most indicative of a confirmed exoplanet disposition and similarly which attributes are most indicative of a false positive disposition. Finally, once these attributes are determined they will be used to produce a reusable machine learning model that can help predict which exoplanet candidates are most likely to be confirmed.

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

| Variable              | Meaning      |
| --------------------- | ------------ |

</details>

___

## Outline of Project Plan
---
### Data Acquisition

<i>pending</i>

**Steps Taken:**


### Data Preparation

<i>pending</i>

**Steps Taken:**


### Exploratory Analysis

<i>pending</i>

**Steps Taken:**


### Modeling

<i>pending</i>

**Steps Taken:**


___

## Conclusion

<i>pending</i>

___

## Instructions For Recreating This Project

<i>pending</i>

[Back to top](#exploring-kepler-exoplanet-data)