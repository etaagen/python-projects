##### source functions that are used in healthSurveyProject.ipynb #####  

# import libraries to help test functions
import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub as kagglehub
from kagglehub import KaggleDatasetAdapter

def kaggleAPI(file, kaggle_repo):
    """
    Function to load a Pandas dataframe using the Kaggle API.
    
    Note dependencies are required to run this function: Kaggle API, kagglehub, and KaggleDatasetAdapter

    Args:
        file = a string with the name of the dataset file (e.g., 'data.csv').
        kaggle_repo = a string representing the Kaggle repository (e.g., 'username/repo-name').

    Returns:
        df = a Pandas dataframe containing the loaded dataset.
    
    Example: 
        demographic = my_functions.kaggleAPI(file = "demographic.csv", kaggle_repo= "cdc/national-health-and-nutrition-examination-survey")
    """
    file_path = file
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        kaggle_repo,
        file_path,
    )
    # Return the dataframe
    return df


