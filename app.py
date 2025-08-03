import streamlit as st
import time
from datetime import datetime
import sqlite3
from openai import OpenAI
import pytz  # For timezone conversion



st.set_page_config(page_title="🎂 Birthday Surprise", layout="wide")

# Main Home Page
st.title("🎉 Happy Birthday, [Sudha]! 🎉")
st.image("confetti.gif", use_container_width=True)

# Background music
st.audio("birthday_song.mp3")

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





st.set_page_config(page_title="Birthday Countdown", page_icon="🎂", layout="centered")
st.title("🎂 Birthday Countdown")

# Define IST timezone
ist = pytz.timezone("Asia/Kolkata")

# Fixed birthday date in IST
birthday_date = ist.localize(datetime(2025, 8, 4, 0, 0, 0))
st.write(f"🎉 Birthday Date: {birthday_date.strftime('%B %d, %Y %I:%M %p IST')}")

# Placeholder for countdown display
countdown_placeholder = st.empty()

while True:
    # Get current IST time
    now = datetime.now(ist)
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










# OPENAI SETUP
openai_api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
client = OpenAI(api_key=openai_api_key) if openai_api_key else None

# ------------------------------

friend_name = "Sudha"


# QUIZ SECTION
# ------------------------------
num = st.number_input("Don't type anything here", min_value=1, max_value=120, value=20)

st.header("🧠 Birthday Quiz Before Wishing")
quiz_questions = [
    {"question": f"What is {friend_name}'s favorite color?", "options": ["Blue", "Green", "Red"], "answer": "Red"},
    {"question": f"What is  {friend_name} favorate number?", "options": [str(num-15), str(num-12), str(num-19)], "answer": str(1)},
    {"question": f"Which hero does {friend_name} like most?", "options": ["Ram", "Ntr", "Balakrishna"], "answer": "Ntr"}
]

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

for i, q in enumerate(quiz_questions):
    user_answer = st.radio(f"Q{i+1}: {q['question']}", q["options"], key=f"quiz_{i}")
    if st.button(f"Check Q{i+1}", key=f"check_{i}"):
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.quiz_score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {q['answer']}")

if st.session_state.quiz_score == len(quiz_questions):
    st.session_state.quiz_completed = True
    st.success("🎯 Quiz Passed! You can now submit your wish.")
else:
    st.info("Complete all questions correctly to unlock the wish box!")

# Check quiz status
if st.session_state.quiz_completed:
    st.success("✅ You have completed the quiz! You can now access the Wishes Wall.")
    
else:
    st.warning("⚠ You must complete the quiz before accessing the Wishes Wall.")

    st.stop()  # This prevents the rest of the page from running if quiz not completed




st.set_page_config(page_title="Virtual Gift Card", page_icon="🎁", layout="centered")

# Title
st.title("💌 Virtual Birthday Gift Card")

# Fixed birthday details
name = "Sudha"  # Change name here
birthday_date = datetime(2025, 8, 4)

# Show card header
st.markdown(
    f"""
    <div style='text-align: center; background: linear-gradient(135deg, #FF9A9E, #FAD0C4); 
                padding: 40px; border-radius: 20px; color: white;'>
        <h1 style='font-size: 50px;'>🎂 Happy Birthday, {name}! 🎂</h1>
        <p style='font-size: 24px;'>Wishing you a day filled with love, laughter, and happiness.</p>
        <p style='font-size: 20px;'>You are my favorite person in the whole world! </p>
        <p style='font-size: 20px;'>On your special day, I just want to say thank you for being the amazing person you are. Happy Birthday! 💖</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Default photo before opening the gift
st.image("hb.gif", caption="🎉 Your Special Day!", use_container_width=True)

# Countdown
now = datetime.now()
remaining = birthday_date - now
if remaining.total_seconds() > 0:
    st.info(f"⏳ Countdown: {remaining.days} days left until her birthday!")
else:
    st.success("🎉 It's her Birthday! Sending love and confetti! 💌")
    st.balloons()

# Virtual gift section
st.subheader("🎁 Your Virtual Gift")
if "gift_opened" not in st.session_state:
    st.session_state.gift_opened = False

if not st.session_state.gift_opened:
    if st.button("🎁 Open Your Gift"):
        st.session_state.gift_opened = True
        st.balloons()
else:
    st.success("💖 Surprise!")
    st.image("sudha.jpg", caption="A Special Gift for You 💌", use_container_width=True)
    




friend_name = "Sudha"
admin_password = st.sidebar.text_input("Admin Password (for deletion)", type="password")

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
# WISH WALL (SQLite Database)
# ------------------------------
st.header("💌 Birthday Wish Wall")

# Wish submission
if st.session_state.quiz_completed:
    wish = st.text_area("Write your wish here...")
    user_name = st.text_input("Your Name")

    

    if st.button("Send Wish"):
        if wish.strip() and user_name.strip():
            cursor.execute("INSERT INTO wishes (name, wish) VALUES (?, ?)", (user_name, wish))
            conn.commit()
            st.success("🎉 Wish added successfully!")
        else:
            st.warning("Please enter both your name and wish.")
else:
    st.warning("🔒 You must pass the quiz before submitting a wish!")

# Display all wishes (PUBLIC)
st.subheader(f"📜 All Wishes for {friend_name}")
cursor.execute("SELECT * FROM wishes")
all_wishes = cursor.fetchall()

if all_wishes:
    for w in all_wishes:
        st.write(f"💌 {w[0]}. **{w[1]}**: {w[2]}")
        if admin_password == "admin123":  # Only admin can delete
            if st.button(f"❌ Delete Wish {w[0]}", key=f"delete_{w[0]}"):
                cursor.execute("DELETE FROM wishes WHERE id=?", (w[0],))
                conn.commit()
                st.warning("Wish deleted! Please refresh the page.")
else:
    st.info("No wishes yet!")




