from flask import Blueprint, request, jsonify
from pycaret.regression import setup, RegressionExperiment
import pandas as pd
import json

ml_processing = Blueprint('preprocessing', __name__)

df: pd.DataFrame = None 
target_column: str = None 

@ml_processing.route('/api/pre_processing', methods=['POST'])
def pre_processing():
  global df
  global target_column

  data = json.loads(request.data)

  # get the file based off the data
  with open(f'./csv_files/{data["file"]}', 'r') as file:
    df = pd.read_csv(file)

  target_column = data['target_column']

  # convert the target column to a numeric value
  df[target_column] = pd.to_numeric(df[target_column], errors='coerce')

  prev_amount = len(df)
  # Drop the rows that have null values
  df.dropna(subset=[target_column], inplace=True)

  rows_removed = prev_amount - len(df)

  # TODO: show which columns had to be removed

  return jsonify(rows_removed)


@ml_processing.route('/api/run_ml_processing', methods=['GET'])
def run_ml_processing():

  ml_setup = setup(data=df, target=target_column)

  return jsonify(ml_setup), 200
