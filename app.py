"""
IoT with AI Internship — Week 3
Streamlit Smart Doorbell Security Dashboard & Event Log
"""

import os
import json
import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Smart Doorbell Dashboard", page_icon="🔔", layout="wide")

st.title("🔔 Raspberry Pi Smart Doorbell Security Monitor")
st.write("Real-time TinyML visitor classification, snapshot log, and security notifications.")

LOG_FILE = "doorbell_events.json"

st.sidebar.header("🎛️ Doorbell Actions")
if st.sidebar.button("🔔 Trigger Doorbell Ring"):
    os.system("python doorbell_ai.py")
    st.sidebar.success("Doorbell Ring Event Processed!")

st.sidebar.markdown("---")
st.sidebar.markdown("📷 **Camera Status:** ACTIVE (Raspberry Pi V2)")
st.sidebar.markdown("🧠 **TinyML Model:** MobileNetV2-TFLite")

# Load Logs
if not os.path.exists(LOG_FILE):
    st.info("No visitor events recorded yet. Click 'Trigger Doorbell Ring' to capture an event!")
else:
    with open(LOG_FILE, "r") as f:
        events = json.load(f)

    if not events:
        st.info("No visitor events recorded.")
    else:
        st.subheader("📋 Recent Visitor Activity Log")
        
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            df = pd.DataFrame(events)
            st.dataframe(df[["timestamp", "visitor_type", "name", "confidence"]], use_container_width=True)

        with col2:
            st.subheader("📸 Latest Visitor Snapshot")
            latest_event = events[0]
            st.markdown(f"**Visitor:** {latest_event['name']}")
            st.markdown(f"**Status:** `{latest_event['visitor_type']}`")
            st.markdown(f"**Timestamp:** {latest_event['timestamp']}")
            
            if os.path.exists(latest_event['snapshot']):
                image = Image.open(latest_event['snapshot'])
                st.image(image, caption=f"Captured Snapshot - {latest_event['visitor_type']}", use_column_width=True)
            else:
                st.warning("Snapshot preview unavailable.")