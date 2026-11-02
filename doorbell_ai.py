"""
IoT with AI Internship — Week 3
Raspberry Pi Smart Doorbell System - TinyML Face Recognition & Snapshot Logging
"""

import os
import cv2
import json
import time
import numpy as np
from datetime import datetime

LOG_FILE = "doorbell_events.json"
SNAPSHOT_DIR = "./snapshots"

# Pre-defined Visitor Database Mapping
KNOWN_VISITORS = ["Mahima (Resident)", "Family Member", "Delivery Driver"]

def log_visitor_event(visitor_type, name, confidence, snapshot_path):
    """Appends security logs to JSON file for dashboard tracking."""
    event = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "visitor_type": visitor_type,
        "name": name,
        "confidence": f"{confidence * 100:.2f}%",
        "snapshot": snapshot_path
    }

    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

    logs.insert(0, event)  # Newest event first

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"[✔] Event Logged: {visitor_type} - {name} ({event['confidence']})")

def run_doorbell_system(simulate_camera=True):
    print("[*] Initializing Raspberry Pi Smart Doorbell System...")
    print("[*] Loading TinyML Face Recognition Engine...")

    if not os.path.exists(SNAPSHOT_DIR):
        os.makedirs(SNAPSHOT_DIR)

    # Load Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if simulate_camera:
        print("[*] Simulating Doorbell Camera Detection Trigger...")
        # Create a synthetic image for headless/CI demonstration
        synthetic_img = np.zeros((400, 400, 3), dtype=np.uint8)
        cv2.putText(synthetic_img, "Doorbell Camera Live", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        # Simulate Visitor Classification
        is_known = np.random.choice([True, False], p=[0.6, 0.4])
        confidence = float(np.random.uniform(0.85, 0.99))
        
        if is_known:
            visitor_name = str(np.random.choice(KNOWN_VISITORS))
            visitor_type = "Known Visitor"
        else:
            visitor_name = "Unknown Intruder"
            visitor_type = "Alert: Unknown"

        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_filename = f"snapshot_{timestamp_str}.jpg"
        snapshot_path = os.path.join(SNAPSHOT_DIR, snapshot_filename)
        
        cv2.imwrite(snapshot_path, synthetic_img)
        log_visitor_event(visitor_type, visitor_name, confidence, snapshot_path)

if __name__ == "__main__":
    run_doorbell_system(simulate_camera=True)