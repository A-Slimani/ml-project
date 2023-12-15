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
    path = './static/temp.csv'
    file.save(path)
    with open(path, newline='') as csv_file:
        headers = next(csv.reader(csv_file))
        print(headers)

        # convert headers into a string that can be run with cypher
        # cypher_headers =  
        

        # with driver.session() as session:
        #     session.run("""
        #         LOAD CSV FROM './static/temp.csv'
        #     """)

    return "success", 200 

if __name__ == '__main__':
    app.run()