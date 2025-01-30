from ChatBotRAG.utils.utils import retrieve_relevant_document
from openai import OpenAI

def handle_query(client: OpenAI, user_query: str) -> str:
    """
    Handle user queries using a Retrieval-Augmented Generation (RAG) approach.

    This function retrieves the most relevant document from the knowledge base
    using the `retrieve_relevant_document` function. It then utilizes OpenAI's
    GPT model to generate a response based on the retrieved document.

    Args:
        client (OpenAI): The OpenAI client instance for making API calls.
        user_query (str): The user's input query.

    Returns:
        str: The generated response from the OpenAI model.
    """
    # Step 1: Retrieve the most relevant document
    relevant_doc = retrieve_relevant_document(user_query)

    if not relevant_doc:
        return "Sorry, I couldn't find any relevant information."


    # Step 2: Use OpenAI GPT to generate a response based on the retrieved document
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a technical support assistant for a software product. "
                           "Only answer questions related to software installation, updates, "
                           "troubleshooting, and licensing."
            },
            {
                "role": "user",
                "content": f"Question: {user_query}\nContext: {relevant_doc['answer']}",
            },
        ],
        max_tokens=150,
    )

    return completion.choices[0].message.content
