import pycaret
import pandas as pd

"""
- Get the csv file from the frontend
- Get the selected target column 
- Return the preprocessed data
"""
def preprocess(csv_file):
    df = pd.read_csv(csv_file) 
