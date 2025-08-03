import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Birthday Countdown", page_icon="🎂", layout="centered")
st.title("🎂 Birthday Countdown")

# Fixed birthday date (non-editable)
birthday_date = datetime(2025, 8, 4, 0, 0, 0)
st.write(f"🎉 Birthday Date: {birthday_date.strftime('%B %d, %Y')}")

# Placeholder for countdown display
countdown_placeholder = st.empty()

while True:
    now = datetime.now()
    remaining = birthday_date - now

    if remaining.total_seconds() <= 0:
        countdown_placeholder.success("🎉 Happy Birthday Sudha! 🎂")
        break
    else:
        days = remaining.days
        hours = (remaining.seconds // 3600)
        minutes = (remaining.seconds % 3600) // 60
        seconds = remaining.seconds % 60

        countdown_placeholder.info(
            f"⏳ Time left: **{days} days, {hours} hours, {minutes} minutes, {seconds} seconds**"
        )

    time.sleep(1)  # Update every second
