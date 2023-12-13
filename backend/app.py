from flask import Flask, render_template
from db import connect_db

app = Flask(__name__, static_folder='static', static_url_path='/assets')

@app.route("/")
def index():
    connect_db() 
    return render_template('index.html')
