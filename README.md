# Stock-Research-Assistant
Streamlit application to help with researching stocks

## Requirements

- Python 3.10.16
- Required Python packages (listed in `requirements.txt`)
- Google API Key for accessing the Gemini AI services
- Pinecone API Key for creating and/or accessing the Pinecone Database

## Installation

1. **Clone the repository**:

     ```bash
     git clone https://github.com/Vish501/Medical-ChatBot.git
    ```
     
     ```bash
     cd Medical-ChatBot
    ```
     
2. **Install dependencies**:

    It's recommended to use a virtual environment to manage dependencies. You can create and activate one using:
   
     ```bash
     conda create -p venv python=3.10.16 -y
    ```
     
     ```bash
    conda activate venv/
   ```
     Then, install the required packages: ```pip install -r requirements.txt```

## Setting Up the Google API Key

To use the Gemini API, you need to set up your GOOGLE_API_KEY:

1. Obtain your **Google API Key** from the **Google Cloud Console**.
2. Add the API key to your environment:
     - Locally (Linux/macOS): ```export GOOGLE_API_KEY="your-api-key-here"```
     - Locally (Windows - Command Prompt): ```set GOOGLE_API_KEY="your-api-key-here"```
     - Locally (Windows - PowerShell): ```$env:GOOGLE_API_KEY="your-api-key-here"```

3. If you are using GitHub Codespaces, store the API key as a GitHub repository secret:
     
     - Go to your GitHub repository
     - Navigate to **Settings > Secrets and variables > Actions**
     - Click **New repository secret**
     - Set the name as ```GOOGLE_API_KEY``` and paste your API key as the value
     - Click **Add secret**

This will allow the chatbot to authenticate and communicate with the Gemini API securely.