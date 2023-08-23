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

# Checkbox for selecting emotions
st.write("Select the emotions you want to infuse:")
emotions = [
    'Gangster 🕶️', 'Angry 😠', 'Friendly 😀', 'Confident 😎',
    'Curious 🤔', 'Caring ❤️', 'Arrogant 😏', 'Loving ❤️',
    'Simple 😊', 'Optimistic 😄', 'Pessimistic 😔', 'Sad 😢',
    'Happy 😃', 'Sincere 😇', 'Cooperative 🤝'
]

selected_roles = []

col1, col2, col3, col4, col5 = st.columns(5)

for idx, emotion in enumerate(emotions):
    column = idx % 5
    with col1 if column == 0 else col2 if column == 1 else col3 if column == 2 else col4 if column == 3 else col5:
        agree = st.checkbox(emotion, key=idx)
        if agree:
            selected_roles.append(emotion)

        

# selected_roles = st.multiselect("Emotions:", emotions, default=['Friendly 😀'])

go_button = st.button("Transform")

# st.subheader("Transformed Text:")

st_cb = StreamHandler(st.empty())
chat = ChatOpenAI(max_tokens=1000, streaming=True, callbacks=[st_cb])

if query and go_button:
    # messages = get_translation_getup(query=query)
    messages = get_mood_getup(query=query, role=selected_roles)
    chat(messages)
