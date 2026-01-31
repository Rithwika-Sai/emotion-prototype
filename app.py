import streamlit as st
from textblob import TextBlob

st.title("Emotion Detection Prototype")
st.write("Emotion detection using text")

text = st.text_input("Enter your message")

if text:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        st.success("Detected Emotion: Happy")
    elif polarity < 0:
        st.error("Detected Emotion: Sad")
    else:
        st.info("Detected Emotion: Neutral")
