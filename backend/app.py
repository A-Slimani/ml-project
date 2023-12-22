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
    path = f"./static/{filename}"
    file.save(path)

    content = ""
    with open(path, newline='') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        for data in reader:
            content += data 

    print(content) 
    print(headers)
    cypher_query = ""

    for header in headers:
        cypher_query += ""

    # with driver.session() as session:
    #     session.run("""
    #         LOAD CSV WITH HEADERS FROM 'file:///static/Australian Vehicle Price.csv' AS LINE 
    #         CREATE (v:Vehicle {make: row.make, model: row.model, price: row.price})
    #     """)
  
    return "success", 200 

if __name__ == '__main__':
    app.run()