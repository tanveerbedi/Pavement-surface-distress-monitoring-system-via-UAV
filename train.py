import cv2
import numpy as np
from ultralytics import YOLO
from pathlib import Path
from tqdm import tqdm

# ------------------------------
# 🔧 1. Load pretrained model
# ------------------------------
model = YOLO('yolov8n.pt')  # yolov8s.pt, yolov8m.pt etc. for more capacity

# ------------------------------
# 🌡 2. Convert RGB to pseudo-thermal image
# ------------------------------
def convert_to_thermal(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thermal = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return thermal

# ------------------------------
# 📦 3. Prepare YOLO dataset (thermal images, in-memory)
# ------------------------------
def load_yolo_dataset(image_dir, label_dir):
    image_paths = sorted(Path(image_dir).glob("*.jpg"))
    label_paths = sorted(Path(label_dir).glob("*.txt"))
    dataset = []

    for img_path in tqdm(image_paths, desc=f"Loading {image_dir}"):
        img = cv2.imread(str(img_path))
        if img is None:
            continue

        thermal_img = convert_to_thermal(img)

        label_path = Path(label_dir) / (img_path.stem + ".txt")
        if not label_path.exists():
            continue

        # Optional: Could validate label format here

        dataset.append((thermal_img, str(label_path)))

    return dataset

# ------------------------------
# 🧠 4. Load the data
# ------------------------------
train_dataset = load_yolo_dataset("datasets/images/train", "datasets/labels/train")
val_dataset = load_yolo_dataset("datasets/images/val", "datasets/labels/val")

# ------------------------------
# 📄 5. Create data.yaml for training config
# ------------------------------
args_yaml = {
    'train': 'datasets/images/train',  # still need image folder paths
    'val': 'datasets/images/val',
    'nc': 1,
    'names': ['pothole']
}

# ------------------------------
# 🚀 6. Train with fine-tuning
# ------------------------------
model.train(
    data=args_yaml,
    epochs=50,
    imgsz=640,
    batch=8,
    workers=2,
    name="yolov8_thermal_finetune",
    pretrained=True,
    verbose=True
)

# ------------------------------
# 🎯 7. After training: inference using confidence threshold
# ------------------------------
test_image = cv2.imread("datasets/images/val/sample.jpg")
thermal_input = convert_to_thermal(test_image)

# Set confidence threshold
results = model.predict(thermal_input, conf=0.5)  # Set your threshold here (e.g., 0.5)
results[0].show()  # Show result with bounding boxes