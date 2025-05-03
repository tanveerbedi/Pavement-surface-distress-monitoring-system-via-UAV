import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
import tempfile

# Load model
@st.cache_resource

def load_model():
    return YOLO("best.pt")

model = load_model()

# Streamlit UI
st.set_page_config(page_title="Pothole Detector", layout="centered")
st.title("Pavement surface distress monitoring system via UAV")

st.markdown("""
Upload a road image 📷 and this app will detect potholes using a trained YOLOv8 segmentation model.
""")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Save uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file.name)
        temp_path = temp_file.name

    # Run detection
    st.info("Detecting potholes...")
    results = model.predict(source=temp_path, save=False, conf=0.4)

    # Show results
    result_image = results[0].plot()
    st.image(result_image, caption="Detection Result", use_container_width=True)

    # Clean up temp file
    os.remove(temp_path)

    st.success("Done!")
