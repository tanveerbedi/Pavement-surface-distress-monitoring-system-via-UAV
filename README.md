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
├── app.py                   # Main app logic
├── areaEstimation.py        # Area calculation script
├── best.pt                  # Trained YOLOv8 model weights
├── detect.py                # Detection script using YOLOv8
├── requirements.txt         # Python dependencies
├── train.py                 # Training script
├── test.yaml                # Testing configuration
├── web_app.py               # Web interface script
├── output/                  # Output image with detections
├── venv/                    # Virtual environment (not included in version control)
├── install.sh / run.sh      # Setup and execution scripts
```

---

## Installation

```bash
git clone https://github.com/<your-username>/UAVpotholes.git
cd UAVpotholes
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
Special thanks to the UAV research team and faculty mentors for their support.
