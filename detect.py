from ultralytics import YOLO

model = YOLO("best.pt")

# Predict on entire folder
results = model.predict(source="groundOnly_pothole/images/val", save=True)

results[0].save(filename="output.jpg")

