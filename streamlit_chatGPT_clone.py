import openai
import streamlit as st
from streamlit_chat import message as st_message


openai.api_key = "Use your api key here"

st.set_page_config(page_title="ChatBot", page_icon=":tada:", layout="wide")
st.title("OpenAI - ChatGPT Clone")

def start_chat():
    response =openai.Completion.create(
    model="text-davinci-003",
    prompt=st.session_state.input_text,
    max_tokens=150,
    temperature=0.9,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0.6
    )
    st.session_state.history.append({'message':st.session_state.input_text, "is_user":True})
    st.session_state.history.append({'message':response.choices[0].text, "is_user": False})

if "history" not in st.session_state:
    st.session_state.history = []

with st.container():
    for chat in st.session_state.history:
        st_message(**chat)

st.sidebar.text_area("Talk to the bot", key='input_text', on_change=start_chat)