import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("AI Chatbot with LangChain 🤖")

# Initialize OpenAI client
try:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("Please set your OpenAI API key in the environment variables.")
        st.stop()
    
    chat = ChatOpenAI(
        temperature=0.7,
        openai_api_key=openai_api_key
    )
except Exception as e:
    st.error(f"Error initializing OpenAI client: {str(e)}")
    st.stop()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        try:
            messages = [
                SystemMessage(content="You are a helpful and knowledgeable AI assistant."),
                HumanMessage(content=prompt)
            ]
            response = chat(messages)
            st.markdown(response.content)
            st.session_state["messages"].append({"role": "assistant", "content": response.content})
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

# Add sidebar with instructions
with st.sidebar:
    st.markdown("""
    ## How to use
    1. Make sure you have set your OpenAI API key
    2. Type your message in the chat input
    3. Press Enter to send
    4. Wait for the AI to respond
    
    ## About
    This chatbot is powered by LangChain and OpenAI.
    """)
