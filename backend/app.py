from flask import Flask, request, render_template
from neo4j import GraphDatabase
from typing import List
from io import BytesIO
import dotenv
import pdb
import csv
import os

app = Flask(__name__, static_folder='static', static_url_path='/assets')

dotenv.load_dotenv()

# handle db connection
URI = os.getenv('NEO4J_URI')
AUTH = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))

driver = GraphDatabase.driver(URI, auth=AUTH)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/file_upload", methods=['POST'])
def file_upload():
    # handles teh file
    file = request.files['file']
    filename = request.files['file'].filename
    path = f"./csv_files/{filename}"
    # TODO: ensure that the folder doesnt have a combined filespace of 100MB

    file.save(path)

    # handle the object name for db creation
    object_name = request.form["text"]

    # create the driver connection to the db
    driver = GraphDatabase.driver(URI, AUTH)

    for row in csv.DictReader(open(path)):
        print(row)

    # return success message
    return "success", 200 

@app.route("/save_to_db", methods=['POST'])
def save_to_db():   

    return "success", 200

if __name__ == '__main__':
    app.run()