<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# DEEPFAKE-DETECTOR 🎯

## Basic Details

### Team Members
- Member 1: SREELEKSHMI WILSON [ADI SHANKARA INSTITUTE OF ENGINEERING AND TECHNOLOGY]

### Project Description
VeriVision is a real-time digital forensic tool designed to detect deepfakes and AI-generated media. In an era where "seeing is no longer believing," VeriVision provides a mathematical "X-ray" for video feeds, helping users distinguish between biological consistency and computational artifacts.

### The Problem statement
Deepfakes pose a massive threat to digital integrity, from misinformation to identity theft. Human perception is easily fooled by AI-generated faces because our brains focus on facial recognition rather than pixel-level patterns. There is a critical need for lightweight, accessible tools that can verify authenticity without requiring expensive servers.

### The Solution

*VeriVision uses OpenCV and Python to perform real-time Spatial Frequency Analysis.
*Canny Edge Detection: The system strips away color to analyze the "skeleton" of the image.
*Edge Density Logic: It calculates the ratio of edge pixels to total pixels. Real humans produce a specific range of "noise" and edge stability.
*Liveness Detection: By monitoring pixel entropy, the tool identifies if a subject is a live person or a flat, static AI-generated file.

---

## Technical Details

Software Technologies

Language: Python 3.x
Computer Vision: OpenCV (cv2)
Numerical Processing: NumPy (Used for matrix calculations of pixel density)
GUI Components: Tkinter (Used for the Windows file upload dialog)

**For Hardware:**

Processor: Intel Core i5 (Optimized for standard consumer laptops)
Camera: Standard 720p/1080p Integrated Webcam
Memory: 8GB RAM (Minimum)
Note: No external GPU is required, making this accessible for low-power devices.

## Features

Real-Time Forensic Scan: Live Canny Edge detection to visualize "pixel jitter."
Dual-View Interface: Side-by-side comparison of the raw evidence vs. the forensic layer.
Dynamic Verdict System: Automated Green/Red labeling based on edge density.
On-Demand Analysis: Keyboard-triggered ('u' key) image upload for pre-saved files.
## Implementation

### For Software:

#### Installation
```bash
pip install streamlit
pip install mediapipe
pip install opencv-python

#### Run
```bash
[python app.py]
```
