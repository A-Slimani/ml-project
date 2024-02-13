from flask import Flask, render_template
from neo4j import GraphDatabase
from routes.file_selection import file_selection_blueprint
from routes.ml_processing import ml_processing
import dotenv
import os

app = Flask(__name__, static_folder='static', static_url_path='/assets')

dotenv.load_dotenv()

# URI = os.getenv('NEO4J_URI')
# AUTH = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))

# driver = GraphDatabase.driver(URI, auth=AUTH)

@app.route("/")
def index():
    return render_template('index.html')

app.register_blueprint(file_selection_blueprint)
app.register_blueprint(ml_processing)

if __name__ == '__main__':
    app.run()