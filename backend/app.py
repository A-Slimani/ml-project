from flask import Flask, request, render_template, send_file, jsonify
from neo4j import GraphDatabase
from typing import List
from io import BytesIO
import dotenv
import pdb
import csv
import os

app = Flask(__name__, static_folder='static', static_url_path='/assets')

dotenv.load_dotenv()

URI = os.getenv('NEO4J_URI')
AUTH = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))

driver = GraphDatabase.driver(URI, auth=AUTH)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/get_files", methods=['GET'])
def get_files():
    files = os.listdir('./csv_files')
    return jsonify(files)

@app.route("/api/get_file_columns/<filename>", methods=['GET'])
def get_file(filename):
    path = f"./csv_files/{filename}"
    with open(path, 'r') as f:
        columns = f.readline().split(',')
    return columns

@app.route("/api/file_and_object_name_upload", methods=['POST'])
def file_and_object_upload():
    file = request.files['file']
    filename = request.files['file'].filename
    path = f"./csv_files/{filename}"
    # TODO: ensure that the folder doesnt have a combined filespace of 100MB

    file.save(path)

    object_name = request.form["text"]

    return "success", 200 

@app.route("/api/file_upload", methods=['POST'])
def file_upload():
    file = request.files['null']
    filename = request.files['null'].filename
    path = f"./csv_files/{filename}"
    # TODO: ensure that the folder doesnt get large

    file.save(path)
    return "success", 200 

@app.route("/api/pre_processing", methods=['GET'])
def pre_processing():
    pass

@app.route("/api/save_to_db", methods=['POST'])
def save_to_db():   
    return "success", 200

if __name__ == '__main__':
    app.run()