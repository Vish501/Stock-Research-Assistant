# Stock-Research-Assistant
The **Stock Research Assistant** is a Python-based Streamlit application designed to assist users in researching stocks by leveraging AI-powered tools. It integrates with Gemini AI services and FAISS for vector search to provide insightful analyses and information on various stocks.

## 🔧 Features

- **AI-Powered Stock Analysis**: Utilizes Gemini AI to fetch and analyze stock-related data.
- **Efficient Vector Search**: Uses **FAISS** for fast and scalable similarity search over stock-related embeddings.
- **Interactive Streamlit Interface**: Provides a user-friendly web interface for seamless interaction.
- **Customizable Research Parameters**: Allows users to tailor their stock research based on specific criteria.

## 🛠️ Requirements

- Python 3.10.16
- Required Python packages (listed in `requirements.txt`)
- Google API Key for accessing the Gemini AI services

## 🚀 Installation

1. **Clone the repository**:

     ```bash
     git clone https://github.com/Vish501/Stock-Research-Assistant.git
    ```
     
     ```bash
     cd Stock-Research-Assistant
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

## 💻 Setting Up the Google API Key

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

## 💻 Usage

To run the application:​

```bash
streamlit run app.py
```

This will launch the Streamlit web interface in your default browser, where you can start researching stocks using the integrated AI tools.

## 📁 Project Structure
- ```app.py```: Main application file for Streamlit.
- ```requirements.txt```: List of required Python packages.
- ```setup.py```: Setup configuration for the project.
- ```template.py```: Contains template code to create the basic project structure.
- ```research/```: Directory for research-related files and data.
- ```src/```: Source code directory containing modules and packages.

## ⚠️ Disclaimer

This application is powered by AI technologies including language models and vector search. While the bot is designed to provide helpful insights, **it may occasionally produce inaccurate, outdated, or incomplete information**.

**Users are strongly advised to do their own research and consult with a qualified financial advisor before making any investment decisions.** The creators of this project are not responsible for any financial losses or actions taken based on the information provided by this tool.

Use this application at your own risk.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🙌 Acknowledgements

- ```Streamlit``` for the interactive web interface.
- ```Gemini AI``` for AI-powered stock analysis.
- ```FAISS``` for efficient similarity search.


Feel free to contribute to this project by submitting issues or pull requests. For any questions or suggestions, please contact ```Vish501```.
