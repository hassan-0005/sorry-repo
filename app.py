
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
}
.hero, .message {
    background: rgba(255,255,255,0.12);
    padding: 28px 20px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.25);
    text-align: center;
    margin-bottom: 20px;
}
h1, h2, h3, p {
    color: white !important;
    text-align: center;
}
.stButton button {
    width: 100%;
    background: #ff4d9d;
    color: white;
    border-radius: 14px;
    border: none;
    min-height: 48px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div style="font-size:65px">🎂🎈🎉</div>
    <h1>HAPPY BIRTHDAY</h1>
    <h1>HARIS ❤️</h1>
    <p>A special day for a special friend!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="message">
    <h2>💖 Dear Haris 💖</h2>
    <p>Happy Birthday, bro! 🥳</p>
    <p>
    May Allah bless you with happiness, good health,
    success, and a beautiful future. Ameen! 🤲
    </p>
    <p>
    May all your dreams come true, may you always
    keep smiling, and may our friendship stay strong
    for years to come. ❤️
    </p>
    <h3>Stay blessed and keep shining! ✨</h3>
</div>
""", unsafe_allow_html=True)

if st.button("🎁 Open Your Birthday Surprise"):
    st.balloons()
    st.snow()
    st.success("Surprise, Haris! You are an amazing friend! ❤️")
    st.markdown("""
    <div class="message">
        <h2>🎉 HAPPY BIRTHDAY, BRO! 🎉</h2>
        <p>Wishing you a year full of success and smiles!</p>
        <h1>🎂❤️🥳</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; padding:20px;">
Made with ❤️ for Haris
</p>
""", unsafe_allow_html=True)
