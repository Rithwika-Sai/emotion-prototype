import streamlit as st

st.title("Emotion Detection Prototype")
st.write("Basic emotion detection using text keywords")

text = st.text_input("Enter your message")

if text:
    text = text.lower()

    if any(word in text for word in ["happy", "good", "great", "love", "excellent"]):
        st.success("Detected Emotion: Happy 😊")

    elif any(word in text for word in ["sad", "bad", "upset", "angry", "stress"]):
        st.error("Detected Emotion: Sad 😔")

    else:
        st.info("Detected Emotion: Neutral 😐")
