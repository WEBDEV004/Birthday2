import streamlit as st
import sqlite3

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

