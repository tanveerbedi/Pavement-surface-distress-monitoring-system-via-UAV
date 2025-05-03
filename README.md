# Pavement Surface Distress Monitoring System via Automated Visual Inspection using UAV: Automation in Highway Maintenance

## Overview

This project focuses on the development of a **Pavement Surface Distress Monitoring System** that leverages UAV (Unmanned Aerial Vehicle) technology for automated visual inspection and detection of surface anomalies such as potholes, cracks, and other forms of distress on road surfaces. By integrating deep learning-based image segmentation and detection models, the system aims to assist in efficient and cost-effective highway maintenance planning.

---

## Objectives

* To automate the detection of potholes and cracks using high-resolution aerial imagery captured via UAVs.
* To estimate the severity and area of detected potholes.
* To generate actionable visual outputs for infrastructure maintenance authorities.
* To reduce manual effort and increase the speed and accuracy of road distress monitoring.

---

## Features

* **YOLOv8-based Segmentation Model** for pothole detection.
* **Area estimation module** to calculate pothole sizes using pixel-area conversion.
* **Web-based interface** for user uploads and detection visualization.
* **Shell automation scripts** for setup and model execution.

---

## Directory Structure

```
UAVpotholes/
├── best.pt                     # Trained YOLOv8 model weights
├── detect.py                   # Script to run detection on input images
├── train.py                    # Training script
├── areaEstimation.py          # Area calculation logic for potholes
├── web_app.py                  # Flask web app backend
├── app.py                      # Entry point for web interface
├── requirements.txt            # Python dependencies
├── install.sh / run.sh         # Setup and execution shell scripts
├── groundOnly_pothole.yaml    # Dataset config for training
├── test.yaml                   # Test dataset config
├── output/                     # Output results from detection
├── torch_test.py              # Torch environment test
├── yolov_experiment.py        # YOLOv8 experiment configuration
```

---

## Installation

```bash
git clone https://github.com/tanveerbedi/Pavement-surface-distress-monitoring-system-via-UAV
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage

### To Run Detection

```bash
python detect.py
```

Make sure your input images are placed correctly or modify the `detect.py` to accept custom input.

### Web Interface

```bash
python web_app.py
```

Then navigate to `http://localhost:5000` to use the visual upload interface.

---

## Model Details

* Model: YOLOv8 (Ultralytics)
* Weights: `best.pt`
* Framework: PyTorch
* Dataset: Custom UAV-based aerial imagery with annotated potholes

---

## Area Estimation

The `areaEstimation.py` script estimates the physical area of detected potholes by mapping image pixels to real-world dimensions using UAV flight metadata and image resolution.

---

## Results

* Average Precision: 85%
* Inference Time: < 50ms per frame (on GPU)
* Area Estimation Error: < 10% (tested against ground-truth measurements)

---

## Future Improvements

* Integration with GIS platforms for geo-tagged pothole mapping
* Incorporation of road crack detection
* Real-time UAV data streaming and edge inference
* Maintenance cost prediction using regression models

---

## License

MIT License. See [LICENSE](LICENSE) for more details.

---

## Acknowledgements

This project is part of the capstone requirement for B.E. Computer Engineering at **Thapar Institute of Engineering & Technology**.
