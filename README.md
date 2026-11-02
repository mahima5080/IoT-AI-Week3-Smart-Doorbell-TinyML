
# Raspberry Pi Smart Doorbell System (IoT with AI — Week 3)

A TinyML-powered Smart Doorbell system built for Raspberry Pi equipped with a camera module. Uses OpenCV face detection and TensorFlow Lite (TFLite) classification to differentiate between known residents/visitors and unknown intruders, logging events and snapshots to an interactive security dashboard[cite: 20].

---

## 📌 Features

- **Hardware Layer:** Raspberry Pi Camera Module with OpenCV image processing[cite: 20].
- **TinyML Classifier:** Lightweight TensorFlow Lite / MobileNetV2 face recognition engine classifying Known vs. Unknown visitors[cite: 20].
- **Event Logging & Alerts:** Automated snapshot generation and timestamped JSON security logs[cite: 20].
- **Streamlit Security Dashboard:** Real-time web UI displaying recent visitor activity logs and snapshot previews[cite: 20].

---



## 📁 Repository Structure

**Plaintext**

```
iot_week3_smart_doorbell/
├── doorbell_ai.py         # TinyML face recognition & camera script
├── app.py                 # Streamlit security monitoring dashboard
├── doorbell_events.json   # Event activity log storage
├── snapshots/             # Captured visitor snapshot directory
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```


## 🚀 How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
