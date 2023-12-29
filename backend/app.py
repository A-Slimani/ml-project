from flask import Flask, request, render_template
from neo4j import GraphDatabase
from io import BytesIO
import dotenv
import csv
import os

app = Flask(__name__, static_folder='static', static_url_path='/assets')

dotenv.load_dotenv()

# handle db 
URI = os.getenv('NEO4J_URI')
AUTH = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))

driver = GraphDatabase.driver(URI, auth=AUTH)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/file_upload", methods=['POST'])
def file_upload():
    file = request.files['file']
    filename = request.files['file'].filename
    path = f"./csv_files/{filename}"
    # check that the folder doesnt have a combined filespace of 100MB
    file.save(path)

    # return success message
    return "success", 200 

@app.route("/save_to_db", methods=['POST'])
def save_to_db():   

    return "success", 200

if __name__ == '__main__':
    app.run()