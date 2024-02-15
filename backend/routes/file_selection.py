from flask import Blueprint, jsonify, request
import os

file_selection_blueprint= Blueprint('file_selection', __name__)

@file_selection_blueprint.route('/api/get_files', methods=['GET'])
def get_files():
  files = os.listdir('./csv_files')
  return jsonify(files), 200


@file_selection_blueprint.route("/api/get_file_columns/<filename>", methods=['GET'])
def get_file(filename):
    path = f"./csv_files/{filename}"
    with open(path, 'r') as f:
        columns = f.readline().split(',')
    return columns


@file_selection_blueprint.route("/api/file_and_object_name_upload", methods=['POST'])
def file_and_object_upload():
    file = request.files['file']
    filename = request.files['file'].filename
    path = f"./csv_files/{filename}"
    # TODO: ensure that the folder doesnt have a combined filespace of 100MB

    file.save(path)

    object_name = request.form["text"]

    return "success", 200 


@file_selection_blueprint.route("/api/file_upload", methods=['POST'])
def file_upload():
    file = request.files['null']
    filename = request.files['null'].filename
    path = f"./csv_files/{filename}"
    # TODO: ensure that the folder doesnt get large

    file.save(path)
    return "success", 200 


@file_selection_blueprint.route("/api/save_to_db", methods=['POST'])
def save_to_db():   
    return "success", 200