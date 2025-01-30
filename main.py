from openai import OpenAI
import os
from dotenv import load_dotenv

from ChatBotRAG.utils.openaiUtils import handle_query
from ChatBotRAG.utils.utils import is_within_scope

# Load environment variables
load_dotenv()

# Set up OpenAI API key
api_key = os.getenv("OPENAI_KEY")  # Ensure this is set in your .env file
client = OpenAI(api_key=api_key)


# Command-line interface for user queries
def main():
    print("Welcome to the AI Support Assistant! Type 'exit' to quit.\n")

    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break

        if not is_within_scope(user_query):
            bot_response = "Sorry, I can only assist with software installation, updates, troubleshooting, and licensing."
        else:
            bot_response = handle_query(client, user_query)

        print(f"Bot: {bot_response}\n")


if __name__ == "__main__":
    main()
