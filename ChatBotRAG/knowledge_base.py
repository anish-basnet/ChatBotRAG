from sklearn.feature_extraction.text import TfidfVectorizer


# Sample knowledge base (FAQs) for software technical support
knowledge_base = [
    {"question": "How do I install the software?", "answer": "You can install the software by downloading the installer from https://example.com/download and following the on-screen instructions."},
    {"question": "How do I update the software?", "answer": "To update the software, open the application, go to Settings > Update, and click 'Check for Updates.'"},
    {"question": "How do I reset my password?", "answer": "You can reset your password by visiting https://example.com/reset-password."},
    {"question": "How do I contact technical support?", "answer": "Please email us at support@example.com or call +1-800-123-4567 for technical support."},
    {"question": "How do I troubleshoot installation errors?", "answer": "Common installation errors can be resolved by ensuring your system meets the minimum requirements and disabling antivirus software during installation."},
    {"question": "How do I activate my license?", "answer": "To activate your license, open the software, go to Settings > License, and enter your activation key."},
]



def get_document_vectors_with_vectorizer():
    # Preprocess knowledge base for retrieval
    documents = [item["question"] for item in knowledge_base]
    vectorizer = TfidfVectorizer()
    document_vectors = vectorizer.fit_transform(documents)
    return vectorizer, document_vectors