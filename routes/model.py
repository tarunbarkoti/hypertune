from flask import Blueprint, request, jsonify, Response, send_file
from services.fine_tune import fine_tune_model
from services.evaluate import evaluate_model
import os

model_bp = Blueprint("model", __name__)

@model_bp.route("/fine-tune-stream", methods=["GET"])
def fine_tune_stream():
    model_name = request.args.get("model_name")
    dataset_path = request.args.get("dataset_path")
    batch_size = int(request.args.get("batch_size", 4))
    epochs = int(request.args.get("epochs", 3))
    learning_rate = float(request.args.get("learning_rate", 5e-5))
    use_spheron = request.args.get("use_spheron", "false").lower() == "true"

    if not model_name or not dataset_path:
        return jsonify({"message": "Missing required fields"}), 400

    def stream():
        for message in fine_tune_model(model_name, dataset_path, batch_size, epochs, learning_rate, use_spheron):
            yield f"data: {message}\n\n"

    return Response(stream(), mimetype="text/event-stream")

@model_bp.route("/download-model/<model_name>", methods=["GET"])
def download_model(model_name):
    model_path = f"models/{model_name}-fine-tuned"
    
    if not os.path.exists(model_path):
        return jsonify({"message": f"Model {model_name} not found!"}), 404

    zip_file = f"{model_path}.zip"
    os.system(f"zip -r {zip_file} {model_path}")
    
    return send_file(zip_file, as_attachment=True)

@model_bp.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    model_path = data.get("model_path")

    if not model_path or not os.path.exists(model_path):
        return jsonify({"message": "Model path required or model not found"}), 400

    metrics = evaluate_model(model_path)
    return jsonify({"metrics": metrics})
