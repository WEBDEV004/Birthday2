import streamlit as st
from datetime import datetime

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
st.image("assets/hb.gif", caption="🎉 Your Special Day!", use_container_width=True)

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
    st.image("assets/sudha.jpg", caption="A Special Gift for You 💌", use_container_width=True)
    
