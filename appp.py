import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# 1. Forensic Logic Function (The Brain)
def analyze_frame(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    
    # Verdict Logic
    edge_density = np.sum(edges) / (img.shape[0] * img.shape[1])
    if edge_density > 8:
        verdict, color = "REAL HUMAN", (0, 255, 0)
    else:
        verdict, color = "SUSPECTED AI / STATIC", (0, 0, 255)
    
    # Visuals
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    combined = np.hstack((img, edges_bgr))
    
    # Draw Verdict Box
    cv2.rectangle(combined, (0, 0), (450, 60), (0,0,0), -1)
    cv2.putText(combined, f"STATUS: {verdict}", (10, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    return combined

# 2. Setup
cap = cv2.VideoCapture(0)
print("SYSTEM ACTIVE: Press 'u' to Upload | Press 'q' to Quit")

while True:
    ret, frame = cap.read()
    if not ret: break

    # Show Live Feed
    display = analyze_frame(frame)
    cv2.imshow('VeriVision Forensic Lab', display)

    key = cv2.waitKey(1) & 0xFF
    
    # --- THE UPLOAD FEATURE ---
    if key == ord('u'):
        root = tk.Tk(); root.withdraw()
        path = filedialog.askopenfilename()
        root.destroy()

        if path:
            img = cv2.imread(path)
            if img is not None:
                img = cv2.resize(img, (640, 480))
                result = analyze_frame(img)
                cv2.imshow('Analysis Result (Any key to close)', result)
                cv2.waitKey(0)
                cv2.destroyWindow('Analysis Result (Any key to close)')

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()