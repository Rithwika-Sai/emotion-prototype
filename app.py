import streamlit as st
from deepface import DeepFace
import cv2
from textblob import TextBlob

st.title("Real-time Emotion Detection System")
st.write("Detecting emotions using Facial Expression and Text")

# -------- TEXT EMOTION --------
st.header("Text Emotion Detection")

user_text = st.text_input("Enter your message:")

def analyze_text(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Happy 😊"
    elif polarity < 0:
        return "Sad 😔"
    else:
        return "Neutral 😐"

if user_text:
    emotion = analyze_text(user_text)
    st.success(f"Detected Emotion from Text: {emotion}")

# -------- FACE EMOTION --------
st.header("Facial Emotion Detection (Webcam)")

run = st.checkbox('Start Camera')

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        st.error("Failed to access camera")
        break

    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    emotion = result[0]['dominant_emotion']

    cv2.putText(frame, f'Emotion: {emotion}', (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

camera.release()

