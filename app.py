import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("Pothole Detector 🚧")
model = YOLO("runs/segment/yolov8Potholes10/weights/best.pt")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    results = model.predict(img, save=True)
    st.image(results[0].plot(), caption="Detected Image", use_container_width=True)
