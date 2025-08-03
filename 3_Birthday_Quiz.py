import streamlit as st
from openai import OpenAI

# OPENAI SETUP
# ------------------------------
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