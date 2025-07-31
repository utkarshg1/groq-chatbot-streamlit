import streamlit as st
from models import get_models, get_response
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Groq LLM App")
st.title("Groq LLM Chat")
st.subheader("by Utkarsh Gaikwad")

# Load available models
models = get_models()
if not models:
    st.error("No models found. Please check your API key or model URL.")
    st.stop()

# Initialize selected model if not already set
if "selected_model" not in st.session_state:
    st.session_state["selected_model"] = models[0]

# Select model using session state key
st.selectbox("Select a model", models, key="selected_model")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Convert message history to LangChain format
    chat_history = []
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            chat_history.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            chat_history.append(AIMessage(content=msg["content"]))

    # Get and stream assistant response
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""

        for chunk in get_response(
            model=st.session_state["selected_model"], history=chat_history
        ):
            if chunk:
                full_response += chunk # type: ignore
                response_container.markdown(full_response)

        # Save assistant message
        st.session_state["messages"].append(
            {"role": "assistant", "content": full_response}
        )
