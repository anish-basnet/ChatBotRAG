from openai import OpenAI
from flask import Flask, request, jsonify
import logging
import os
from dotenv import load_dotenv

from ChatBotRAG.utils.openaiUtils import handle_query
from ChatBotRAG.utils.utils import retrieve_relevant_document, is_within_scope

# Load environment variables
load_dotenv()

# Set up OpenAI API key
api_key = os.getenv("OPENAI_KEY")  # Ensure this is set in your .env file
client = OpenAI(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# REST API endpoint for chat
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_query = data.get("message")

    if not user_query:
        return jsonify({"error": "Missing 'message' field in request body"}), 400

    logger.info(f"User query: {user_query}")

    try:
        if not is_within_scope(user_query):
            bot_response = "Sorry, I can only assist with software installation, updates, troubleshooting, and licensing."
            logger.info("Out-of-scope query detected.")
        else:
            bot_response = handle_query(client, user_query)
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        bot_response = "Sorry, I encountered an error while processing your request."

    return jsonify({"response": bot_response})


# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
