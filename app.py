
import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Haris",
    page_icon="🎂",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #16002b, #642080, #e84393);
    color: white;
}

.block-container {
    max-width: 800px;
    padding-top: 3rem;
    padding-bottom: 2rem;
}

.hero, .message {
    background: rgba(255, 255, 255, 0.12);
    padding: 28px 20px;
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.25);
    text-align: center;
    margin-bottom: 20px;
}

h1, h2, h3, p {
    color: white !important;
    text-align: center;
}

.stButton button {
    width: 100%;
    min-height: 48px;
    background: linear-gradient(90deg, #ff4d9d, #ff8c42);
    color: white;
    border-radius: 14px;
    border: none;
    font-weight: bold;
    font-size: 17px;
}

.stButton button:hover {
    border: 1px solid white;
    color: white;
}

.footer {
    text-align: center;
    padding: 20px;
    color: #ffe1f2;
}

@media (max-width: 600px) {
    .block-container {
        padding-top: 1.5rem;
    }
    .hero, .message {
        padding: 20px 12px;
    }
}
</style>
""", unsafe_allow_html=True)

# Main birthday section
st.markdown("""
<div class="hero">
    <div style="font-size: 65px;">🎂🎈🎉</div>
    <h1>HAPPY BIRTHDAY</h1>
    <h1>HARIS ❤️</h1>
    <p style="font-size: 19px;">
        Today is all about you! ✨
    </p>
</div>
""", unsafe_allow_html=True)

# Friendship message
st.markdown("""
<div class="message">
    <h2>💖 Dear Haris 💖</h2>
    <p>Happy Birthday, bro! 🥳</p>
    <p>
        May Allah bless you with happiness, good health,
        success, and a beautiful future. Ameen! 🤲
    </p>
    <p>
        May all your dreams come true, and may you
        always have reasons to smile.
    </p>
    <p>
        Thank you for being an amazing friend.
        May our friendship stay strong forever! ❤️🤝
    </p>
    <h3>Stay blessed and keep shining! 🌟</h3>
</div>
""", unsafe_allow_html=True)

# Birthday surprise
if "surprise_open" not in st.session_state:
    st.session_state.surprise_open = False

if st.button("🎁 Open Your Birthday Surprise"):
    st.session_state.surprise_open = True

if st.session_state.surprise_open:
    st.balloons()

    st.markdown("""
    <div class="message">
        <h1>🎉 SURPRISE, HARIS! 🎉</h1>
        <h2>You are an amazing friend! ❤️</h2>
        <p>
            May this new year of your life bring
            happiness, success, and countless memories.
        </p>
        <p>Keep smiling, keep winning, and stay blessed! 🤲</p>
        <h1>🎂🥳🎈</h1>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🎊 Celebrate Again"):
        st.session_state.surprise_open = False
        st.rerun()

# Footer
st.markdown("""
<div class="footer">
    Made with ❤️ for Haris<br>
    A special birthday gift from a friend 🎁
</div>
""", unsafe_allow_html=True)
