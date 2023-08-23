from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from utils.streaming import StreamHandler
from utils.sidebar import sidebar
from dotenv import load_dotenv

from tones.translation import message_generator as get_translation_getup
from tones.tones_getup import message_generator as get_mood_getup

load_dotenv()

# Set magical theme
st.set_page_config(
    page_title="ToneWizard - Enchanted Tone Transformation",
    page_icon="🌟✨",
    layout="wide",
)

# sidebar()

# st.title("ToneWizard - Transform Your Text's Emotion")

query = st.text_area(
    "Enter your text:", placeholder="Hello, how are you?", height=200)

role = st.radio("Select the emotion you want to infuse:",
    options=('Gangster 🕶️', 'Angry 😠', 'Friendly 😀', 'Confident 😎', 'Curious 🤔', 'Caring ❤️', 'Arrogant 😏', 'Loving ❤️', 'Simple 😊', 'Optimistic 😄', 'Pessimistic 😔', 'Sad 😢', 'Happy 😃', 'Sincere 😇', 'Cooperative 🤝'),
    index=0,
    disabled=False,
    horizontal=True,
    label_visibility="visible")


go_button = st.button("Transform")

# st.subheader("Transformed Text:")

st_cb = StreamHandler(st.empty())
chat = ChatOpenAI(max_tokens=1000, streaming=True, callbacks=[st_cb])

if query and go_button:
    # messages = get_translation_getup(query=query)
    messages = get_mood_getup(query=query, role=role)
    chat(messages)
