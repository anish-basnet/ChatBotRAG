# AI Powered Customer Support Chatbot

Your chatbot is designed to assist users with common software-related queries, specifically focused on installation, updates, troubleshooting, licensing, and support. Here’s a breakdown of the key areas it covers:

### Software Installation

Users can download the installer from example.com and follow the on-screen instructions.
### Software Updates

Updates can be checked via Settings > Update within the software.
### Password Reset

Users can reset their password by visiting example.com/reset-password.
### Technical Support

Support is available via email (support@example.com) or phone (+1-800-123-4567).
### Troubleshooting Installation Errors

Users should check system requirements and disable antivirus software if they face issues during installation.
### License Activation

Activation requires navigating to Settings > License and entering an activation key.
### Functionality Overview
- Retrieves the most relevant response using TF-IDF & Cosine Similarity.
- Filters queries to ensure relevance to software-related topics.
- Generates AI-powered responses based on predefined answers.


## Installation Guide

### Prerequisites
Make sure you have the following installed on your system:

- Python 3.x (Download from [python.org](https://www.python.org/downloads/))
- Git (Download from [git-scm.com](https://git-scm.com/))

### Steps to Install

1. **Clone the Repository**:
   First, clone the project repository to your local machine. Open your terminal or command prompt and run the following command:
   ```bash
   git clone https://github.com/anish-basnet/ChatBotRAG.git
   ```
2. **Navigate to the Project Directory**:
   After cloning the repository, go to the project directory:
   ```bash
   cd ChatBotRAG
   ```
   
3. **Create a Virtual Environment (Optional but recommended)**:
   It's a good practice to use a virtual environment to manage dependencies. To create a virtual environment, run the following command:
   ```bash
   python -m venv venv
   ```
   
4. **Activate the Virtual Environment**:
   * On windows:

    ```bash
       .\venv\Scripts\activate
    ```
   * On Linux/macOS

    ```bash
       source venv/bin/activate
    ```
5. ** Install Dependencies**:
   The project may have a requirements.txt file that lists the necessary dependencies. To install them, run:
   ```bash
   pip install -r requirements.txt
   ```
   
6. **Create .env file**:
    After this .env file has to be created and add the openAI key and API key as follow,

```document
    API_KEY=13234aakif113
    OPENAI_KEY=sk-proj-ajdfaisdfiakdfaksfakdkd
```

7. ** Run the Project**:
   After installing the dependencies and .env file, you can run the project. For example, if there is a script you want to run, use:
   ```bash
    python main.py
   ```