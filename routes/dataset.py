import os
from flask import Blueprint, request, jsonify

dataset_bp = Blueprint("dataset", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@dataset_bp.route("/upload", methods=["POST"])
def upload_dataset():
    if "file" not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"message": "No selected file"}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, "dataset.csv")
    file.save(file_path)
    
    return jsonify({"message": "Dataset uploaded successfully!"})
