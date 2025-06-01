# Robotic Arm Project — Color-Based Object Detection and Pick-and-Place (BeagleBone Blue)

A low-cost, edge-based robotic arm system using a USB camera and BeagleBone Blue. This project identifies objects based on color using computer vision and controls a 4-axis robotic arm through I2C-enabled servo driver or direct PWM outputs for pick-and-place tasks.

---

## Project Highlights

* Real-time **color detection** using OpenCV
* Object shape analysis with contour filtering
* 4-axis **servo-driven robotic arm** control
* I2C-based servo driver (PCA9685) or direct PWM
* Fully integrated with **BeagleBone Blue**
* USB camera + live image processing
* Wireless SSH/VNC + SD card expansion

---

## System Overview

```mermaid
flowchart TD
    CAM[USB Camera] --> BBB[BeagleBone Blue]
    BBB --> CV[Color Detection (OpenCV)]
    CV --> Classifier[Color Classifier]
    Classifier --> Controller[Motion Controller]
    Controller --> Driver[Servo Driver Board (I2C)]
    Driver --> AR[4-Axis Robotic Arm]
```

---

## Hardware Setup

| Component              | Purpose                     |
| ---------------------- | --------------------------- |
| BeagleBone Blue        | Edge controller             |
| USB Camera             | Visual input                |
| Servo Driver (PCA9685) | PWM signal generator        |
| 4x Servo Motors        | Control arm joints          |
| Breadboard + JST       | Signal distribution         |
| External 5V Power      | Powers servos independently |
| 16GB SD Card           | System expansion            |

📘 Full setup instructions: [BeagleBone Blue Setup Guide](beaglebone_setup.md)

---

## 💻 Software Overview

* `color_detection.py` — Real-time HSV filtering and mask generation
* `color_classifier.py` — Classifies colors using HSV ranges
* `main.py` — Integrates detection and triggers servo positions

### 📁 Folder Structure

```
roboarm-project/
├── color_detection.py
├── color_classifier.py
├── main.py
├── motion_controller.py
├── requirements.txt
├── README.md
├── beaglebone_setup.md
├── assets/
│   ├── beagleboneBlue_pinout.jpg
│   ├── pca9685_with_arduino_servo.jpg
│   ├── hardware_connection.jpg
│   ├── demo_detection.gif
│   ├── demo_full_connection.gif
│   ├── object&color_detection_output.jpg
│   ├── bbb_servo_output_test.mp4
│   ├── arm_workspace_diagram.jpg
│   ├── bbb_webcam_demo_gui.jpg
│   ├── sevo_driver_pca9685.jpg
```

---

## 🖼️ Results & Demonstration

### 🎯 Color Detection Output

![Detection](assets/object_detection_output.jpg)

### 🤖 Full Robotic Arm Setup

![Setup](assets/setup_photo.jpg)

### 🛠️ Hardware Connection Diagram

![Diagram](assets/hardware_connection_diagram.svg)

### 🎬 Live Demos

#### Color & Object Detection

![Color Detection](assets/demo_detection.gif)

#### Full Arm Movement (I2C-based Control)

![Full Connection](assets/demo_full_connection.gif)

---

## ⚡ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/roboarm-project.git
cd roboarm-project
```

### 2. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Run the Main Script

```bash
python3 main.py
```

---

## 📦 Requirements

See [`requirements.txt`](requirements.txt) for all Python + hardware-related dependencies.

---

## 🧪 Additional Utilities

* `rc_test_servos` — test individual servo channels
* `fswebcam` — image testing via CLI
* VNC for GUI access on BeagleBone Blue

---

## 📌 Notes

* Used Arduino for early arm functionality testing
* LED blinking verified GPIO setup on BBB
* Wi-Fi configured for wireless SSH/VNC
* Storage expanded using a 16GB SD card

---

## 🙋‍♂️ Author

**Pawan**
Robotics + AI Developer
✉️ \[LinkedIn/GitHub/Website links if available]

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
