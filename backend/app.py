from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static', static_url_path='/assets')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/file_upload", methods=['POST'])
def file_upload():
    file = request
    print(file.files['file'])
    return "success", 200 

if __name__ == '__main__':
    app.run()