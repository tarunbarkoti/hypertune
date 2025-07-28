from flask import Blueprint, request, jsonify
from services.evaluate import evaluate_model

evaluation_bp = Blueprint("evaluation", __name__)

@evaluation_bp.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    model_path = data.get("model_path")

    if not model_path:
        return jsonify({"message": "Model path required"}), 400

    metrics = evaluate_model(model_path)
    return jsonify({"metrics": metrics})
