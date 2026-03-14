## Hand Gesture Mouse Control

a computer vision application that allows controlling the mouse using hand movements captured from a webcam.  
The system tracks hand landmarks in real time and maps hand position and gestures to cursor movement and mouse clicks.

This project was built to explore real-time computer vision, gesture recognition, and human–computer interaction using Python.

---

## Features

- Real-time hand tracking using MediaPipe
- Cursor movement mapped to hand position
- Mouse click detection using a thumb–index pinch gesture
- Live visualization of detected hand landmarks
- Lightweight Python implementation

---

## Technologies Used

- **Python**
- **MediaPipe** – hand landmark detection
- **OpenCV** – webcam capture and visualization
- **PyAutoGUI** – controlling the system mouse

---

## How It Works

1. The webcam captures live video frames.
2. MediaPipe detects **21 hand landmarks** in each frame.
3. The hand position is mapped to **screen coordinates**.
4. The cursor moves according to the tracked hand position.
5. When the **thumb and index finger pinch together**, a mouse click is triggered.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mohprog20/clickWithHandVisualisation.git
cd clickWithHandVisualisation
```
Install the dependencies:
```bash
pip install opencv-python mediapipe pyautogui
Running the Project
```
Run the program:
```bash
python main.py
```
Make sure your webcam is enabled.
