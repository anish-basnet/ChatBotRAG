from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ChatBotRAG.knowledge_base import knowledge_base, get_document_vectors_with_vectorizer
from typing import Dict



def retrieve_relevant_document(query: str) -> Dict[str, str]:
    """
    Retrieve the most relevant document from the knowledge base based on the given query.

    This function uses TF-IDF vectorization to transform the documents and the query into numerical
    representations. It then calculates the cosine similarity between the query and the documents
    to determine the most relevant document.

    Args:
        query (str): The user input query.

    Returns:
        Dict[str, str]: The most relevant document from the knowledge base.
    """
    vectorizer, document_vectors = get_document_vectors_with_vectorizer()
    query_vector = vectorizer.transform([query])  # Use the same vectorizer instance
    similarities = cosine_similarity(query_vector, document_vectors)
    most_relevant_index = similarities.argmax()
    return knowledge_base[most_relevant_index]

def is_within_scope(query: str) -> bool:
    """
    Check if the given query falls within the chatbot's scope.

    This function determines if the query is relevant to software technical support by checking
    for the presence of specific keywords.

    Args:
        query (str): The user input query.

    Returns:
        bool: True if the query is within scope, False otherwise.
    """
    keywords = ["install", "update", "password", "support", "troubleshoot",
                "license", "error", "software", "activate", "technical"]
    return any(keyword in query.lower() for keyword in keywords)
