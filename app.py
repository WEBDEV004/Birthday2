import streamlit as st
import time
import sqlite3

st.set_page_config(page_title="🎂 Birthday Surprise", layout="wide")

# Main Home Page
st.title("🎉 Happy Birthday, [Sudha]! 🎉")
st.image("assets/confetti.gif", use_container_width=True)

# Background music
st.audio("assets/birthday_song.mp3")

# Animated greeting
st.markdown(
    "<h2 style='text-align:center; color:#DA49D4;'>Wishing you a day filled with love, laughter & joy! 🎁</h2>",
    unsafe_allow_html=True
)

# DATABASE SETUP
# ------------------------------
conn = sqlite3.connect("wishes.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS wishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    wish TEXT NOT NULL
)
""")
conn.commit()

# ------------------------------
# SIDEBAR
# ------------------------------
st.sidebar.title("🎈 Birthday Settings")
friend_name = "Sudha"
bg_color = st.sidebar.color_picker("Choose Theme Color", "#FDC9C9")
admin_password = st.sidebar.text_input("Admin Password (for deletion)", type="password")

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {bg_color};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)