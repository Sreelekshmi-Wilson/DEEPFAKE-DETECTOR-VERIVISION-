Project Name: VeriVision
Tagline: Making the invisible flaws of AI visible.

** Overview

VeriVision is a real-time digital forensic tool designed to detect deepfakes and AI-generated media. In an era where "seeing is no longer believing," VeriVision provides a mathematical "X-ray" for video feeds, helping users distinguish between biological consistency and computational artifacts.

** The Problem

Deepfakes pose a massive threat to digital integrity, from misinformation to identity theft. Human perception is easily fooled by AI-generated faces because our brains focus on facial recognition rather than pixel-level patterns. There is a critical need for lightweight, accessible tools that can verify authenticity without requiring expensive servers.

** How it Works (Technical)

VeriVision uses OpenCV and Python to perform real-time Spatial Frequency Analysis.
Canny Edge Detection: The system strips away color to analyze the "skeleton" of the image.
Edge Density Logic: It calculates the ratio of edge pixels to total pixels. Real humans produce a specific range of "noise" and edge stability.
Liveness Detection: By monitoring pixel entropy, the tool identifies if a subject is a live person or a flat, static AI-generated file.

** Key Features

Dual-View Analysis: Side-by-side comparison of the original feed and the forensic scan.
Instant Verdict: Real-time "Verified Human" or "Suspected AI" status indicators.
Universal Upload: A built-in feature to analyze existing images or videos (using the 'u' key).
Hardware Optimized: Designed to run smoothly on standard laptops (like the Lenovo i5) without needing a GPU.

** Future Scope

Biometric Integration: Adding R-PPG to detect a human pulse through the webcam.
Mobile Port: Developing a Flutter/TensorFlow Lite app for on-the-go verification.
Browser Plugin: Integrating VeriVision directly into Zoom and WhatsApp to protect users during live calls.
