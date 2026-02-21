![Uploading image.png…]()


### **Basic Details**

* **Team Members:** Member 1: **Sreelekshmi Wilson** - ADI SHANKARA INSTITUTE OF ENGINEERING AND TECHNOLOGY
* **Project Description:** VeriVision is a real-time deepfake detection tool that uses mathematical edge analysis to distinguish between live human subjects and AI-generated or static media.

---

### **The Problem Statement**

With the rise of generative AI, deepfakes have become a major threat to digital security and trust. Human eyes often fail to detect pixel-level inconsistencies in synthetic media, leading to potential identity theft and misinformation. There is a critical need for lightweight, real-time forensic tools that can verify liveness without requiring heavy server-side processing.

---

### **The Solution**

**VeriVision** provides a "Digital X-Ray" for video feeds. By utilizing the Canny Edge Detection algorithm, it strips away visual textures to analyze the structural integrity and "pixel jitter" of a subject. The system calculates a real-time **Edge Density Index** to provide an instant liveness verdict, successfully flagging static photos or AI-rendered overlays that lack natural biological entropy.

---

### **Technical Details**

#### **Technologies & Components Used**

**For Software:**

* **Languages:** Python 3.11
* **Libraries:** OpenCV (`cv2`), NumPy
* **Tools:** VS Code, Git/GitHub, Tkinter (for file dialogs)

**For Hardware:**

* **Main components:** Standard Laptop (Lenovo i5), Integrated HD Webcam (720p/1080p).
* **Specifications:** Optimized for CPU-only inference (no external GPU required).

---

### **Features**

* **Feature 1: Real-time Forensic Overlay** – Side-by-side view of the raw camera feed and the Canny Edge analysis.
* **Feature 2: Dynamic Verdict System** – Automated "VERIFIED HUMAN" (Green) or "SUSPECTED AI" (Red) status labels.
* **Feature 3: On-Demand Image Upload** – A keyboard-triggered ('u' key) interface to analyze existing image files from local storage.
* **Feature 4: Biological Entropy Tracking** – Uses edge density math to detect the subtle "noise" present in live video but absent in flat AI renders.

---

### **Implementation**

**For Software:**

* **Installation:** `pip install opencv-python numpy`
* **Run:** `python app.py`

**Application Workflow:**

1. **Input:** Captures BGR frames from the system webcam.
2. **Process:** Converts frames to grayscale and applies the Canny algorithm to isolate gradients.
3. **Analysis:** Calculates the ratio of edge pixels to the total frame area.
4. **Output:** Displays the live "Verdict" and a dual-pane forensic visualization.

---

### **Future Enhancements**

1. **R-PPG Integration:** Implementing Remote Photoplethysmography to detect a human pulse through skin-tone changes.
2. **Temporal Consistency:** Adding eye-blink and facial muscle micro-expression tracking to improve accuracy against high-end deepfakes.
3. **Mobile Portability:** Converting the Python logic into a TensorFlow Lite model for a mobile-first "Truth Filter" app.
