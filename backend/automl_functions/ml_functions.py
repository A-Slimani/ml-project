"""
This file is to setup pycaret environment
"""
import pycaret
import pandas as pd

def automl_regression():
  # get which file needed to run from the frontend
  data = pd.read_csv('../csv_files/current.csv')

  # clean non numerical values
  # how to get this value from the frontend?
  data['placeholder'] = pd.to_numeric(data['placeholder'], errors='coerce')
  
    