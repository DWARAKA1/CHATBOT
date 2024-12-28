# AI Chatbot with LangChain

A simple yet powerful chatbot built using LangChain and OpenAI.

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install langchain python-dotenv openai streamlit
   ```

2. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your-api-key-here`

3. Run the chatbot:
   ```bash
   streamlit run chatbot.py
   ```

## Features
- Interactive chat interface using Streamlit
- Powered by OpenAI's language models
- Clean and modern UI
- Chat history persistence during session
- Error handling and user feedback

## Requirements
- Python 3.8+
- OpenAI API key
- Required packages listed in requirements.txt