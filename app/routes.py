from flask import Blueprint, request, jsonify
from .openai_service import ask_chatgpt

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"error": "Falta el mensaje"}), 400

    try:
        response = ask_chatgpt(user_message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
