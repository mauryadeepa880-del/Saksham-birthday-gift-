import streamlit as st
import time
import os

# 1. Page Settings
st.set_page_config(page_title="For Saksham Chaturvedi ❤️", page_icon="🎁", layout="centered")

# 2. Advanced 3D Neumorphism & Luxury Crimson Birthday Theme CSS
st.markdown("""
    <style>
    /* Ultra-Modern Dark Velvet Crimson Layered Background */
    .stApp {
        background: radial-gradient(circle at center, #5c0011 0%, #2b0008 70%, #120003 100%);
        color: #ffffff;
    }
    h1, h2, h3, p, label {
        font-family: 'Poppins', sans-serif;
        text-shadow: 2px 4px 10px rgba(0, 0, 0, 0.5);
    }

    /* Elegant 3D Floating Glass Envelope Container */
    .envelope-box {
        background: linear-gradient(135deg, rgba(255, 75, 75, 0.15), rgba(255, 255, 255, 0.05));
        border: 2px solid rgba(255, 255, 255, 0.25);
        box-shadow: 
            0 20px 50px rgba(0, 0, 0, 0.6),
            inset 0 0 20px rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 40px 30px;
        text-align: center;
        margin-bottom: 25px;
        transform: perspective(1000px) rotateX(12deg) translateY(0px);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    .envelope-box:hover {
        transform: perspective(1000px) rotateX(0deg) translateY(-8px);
        box-shadow: 
            0 30px 60px rgba(255, 75, 75, 0.25),
            inset 0 0 30px rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 235, 59, 0.6);
    }

    /* Premium Thick 3D Tactile Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #ff4b72, #d60032) !important;
        color: #ffffff !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        box-shadow: 
            0 8px 0 #9e0022, 
            0 15px 25px rgba(0, 0, 0, 0.4) !important;
        font-weight: 800 !important;
        font-size: 1.25rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 16px 32px !important;
        transition: all 0.1s ease-in-out;
        width: 100%;
    }
    .stButton>button:hover {
        color: #ffeb3b !important;
        transform: translateY(2px);
        box-shadow: 
            0 6px 0 #9e0022, 
            0 10px 20px rgba(255, 75, 72, 0.3) !important;
        filter: brightness(1.15);
    }
    .stButton>button:active {
        transform: translateY(8px) !important;
        box-shadow: 
            0 0px 0 #9e0022, 
            0 4px 10px rgba(0, 0, 0, 0.3) !important;
    }

    /* 3D Gold-Lined Birthday Document Card */
    .letter-card {
        background: linear-gradient(135deg, #fffcf0 0%, #fff5d1 100%) !important;
        padding: 30px !important;
        border-radius: 20px !important;
        box-shadow: 
            0 15px 40px rgba(0, 0, 0, 0.6),
            inset 0 0 0 6px rgba(212, 175, 55, 0.3) !important;
        border-left: 8px solid #ff4b4b !important;
        text-align: center !important;
        margin-top: 20px;
    }

    /* Forces absolute text contrast inside the pop-up cards */
    .letter-card h1, .letter-card h2, .letter-card h3, .letter-card p, .letter-card b, .letter-card span, .letter-card div {
        color: #2b0008 !important;
        text-align: center !important;
        text-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Helper function to find photos safely
def find_img(base_name):
    for ext in [".png", ".jpg", "", ".jpeg"]:
        if os.path.exists(base_name + ext):
            return base_name + ext
    return None

# Initialize navigation and session variables safely
if "step" not in st.session_state:
    st.session_state.step = "envelope"
if "candle_blown" not in st.session_state:
    st.session_state.candle_blown = False

# --- PHASE 1: THE TEXT ENVELOPE ---
if st.session_state.step == "envelope":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div class='envelope-box'>
            <h1 style='font-size: 3rem; color: #ffeb3b;'>✉️ Secret Delivery</h1>
            <p style='font-size: 1.4rem; font-weight: 500;'>Exclusively Configured For:</p>
            <h2 style='font-size: 2.2rem; letter-spacing: 2px; color: #ffffff;'>SAKSHAM CHATURVEDI</h2>
            <hr style='border-color: rgba(255,255,255,0.1); margin: 25px 0;'>
            <h2 style='font-size: 4.5rem; margin: 10px 0;'>📩</h2>
            <p style='font-size: 1.1rem; opacity: 0.8; font-style: italic;'>Click below to break the structural seal and slide open the message container.</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Open Envelope Seal 🔓"):
        st.session_state.step = "countdown"
        st.rerun()

# --- PHASE 2: AUTOMATIC COUNTDOWN TIMER ---
elif st.session_state.step == "countdown":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1>🎬 Initializing Birthday Module...</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 5rem;'>⏳</h2>", unsafe_allow_html=True)

    countdown_placeholder = st.empty()
    for i in range(3, 0, -1):
        countdown_placeholder.markdown(f"<h2 style='color: #ffeb3b; font-size: 4.5rem; font-weight: bold;'>00 : 00 : 0{i}</h2>", unsafe_allow_html=True)
        time.sleep(1)

    st.balloons()
    st.success("💥 LOUNGE ACCESS DEPLOYED!")
    time.sleep(1)
    if st.button("Enter Special Lounge 💫"):
        st.session_state.step = "gift"
        st.rerun()

# --- PHASE 3: THE MAIN INTERACTIVE HUB (AUTOPLAYS MUSIC) ---
elif st.session_state.step == "gift":
    st.markdown("<h1 style='font-size: 3.2rem; color: #ffeb3b;'>🎂 HAPPY BIRTHDAY, SAKSHAM! 🎂</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.25rem; font-style: italic;'>Happy birthday to you ji, cake-shake hai toh phir jaldi se bulao ji! 🥳🎵</p>", unsafe_allow_html=True)

    # SYSTEM MUSIC STREAM INJECTION
    audio_file_path = "song.mp3.mp3"
    if not os.path.exists(audio_file_path):
        audio_file_path = "song"

    if os.path.exists(audio_file_path):
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", loop=True, autoplay=True)

    st.write("Interact with the floating 3D control boxes below to display your secrets:")
    st.markdown("<br>", unsafe_allow_html=True)

    # Structural 3D Columns
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("💌 Box 1: Identity"):
            st.session_state.active_gift = "identity"
    with col2:
        if st.button("📸 Box 2: Memories"):
            st.session_state.active_gift = "memories"
    with col3:
        if st.button("🕯️ Box 3: Wish"):
            st.session_state.active_gift = "wish"

    # Conditional Layout Canvas Output
    if "active_gift" in st.session_state:
        st.markdown("<br><hr style='border: 1px dashed rgba(255,75,72,0.4);'><br>", unsafe_allow_html=True)

        # --- BOX 1: THE IDENTITY CARD ---
        if st.session_state.active_gift == "identity":
            st.markdown("""
                <div class='letter-card'>
                    <h3 style='font-size: 1.4rem; letter-spacing: 1px;'>👑 OFFICIAL BROTHERHOOD VERIFICATION</h3>
                    <h2 style='font-size: 2.3rem; font-weight: 800; margin: 10px 0;'>Saksham Chaturvedi</h2>
                    <p style='font-size: 1.15rem; line-height: 1.6;'>Current Status: <b>More than just a standard school friend, closer than a biological brother.</b> 🛡️</p>
                    <p style='font-style: italic; font-size: 0.95rem; opacity: 0.75; margin-top: 15px;'>
                    "This virtual space is custom engineered and dedicated entirely to you on your special day."
                    </p>
                </div>
            """, unsafe_allow_html=True)

        # --- BOX 2: MEMORIES ---
        elif st.session_state.active_gift == "memories":
            st.markdown("""
                <div class='letter-card' style='margin-bottom: 30px;'>
                    <h3 style='font-size: 1.4rem;'>🎉 Celebrating 4 Years of Unbreakable Bond</h3>
                    <p style='font-size: 1.15rem; line-height: 1.6;'>Can you believe we have been running side-by-side ever since the <b>6th grade</b>? 🤯</p>
                    <p style='font-size: 1.15rem; line-height: 1.6;'>From studying together, sharing moments, to completely holding it down right now in school—we have grown up together. Today is a celebration of your birthday! Check out these awesome clicks:</p>
                </div>
            """, unsafe_allow_html=True)

            # FIXED IMAGE COLUMN LAYOUT - PREVENTS TYPEERRORS BY INDEXING PROPERLY
            p1 = find_img("photo1")
            p2 = find_img("photo2")
            p3 = find_img("photo3")

            img_cols = st.columns(3)
            if p1: img_cols[0].image(p1, caption="Day Outing ⚡", use_container_width=True)
            if p2: img_cols[1].image(p2, caption="Brotherhood ✨", use_container_width=True)
            if p3: img_cols[2].image(p3, caption="Celebrations 🎉", use_container_width=True)

        # --- BOX 3: WISH CONTROLLER ---
        elif st.session_state.active_gift == "wish":
            st.markdown("<h3 style='text-align: center; color: white !important;'>🕯️ Blow the Birthday Candle</h3>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 5.5rem; text-align: center; margin: 10px 0;'>🎂</p>", unsafe_allow_html=True)

            # THE ULTIMATE TAP BUTTON & CONFETTI PEARLS INJECTION
            if not st.session_state.candle_blown:
                if st.button("💨 TAP HERE TO BLOW OUT THE CANDLE"):
                    st.session_state.candle_blown = True
                    st.rerun()

            # Checkbox blowout toggle switch
            candle_blown = st.checkbox("🕯️ Check this box to blow out the candle and make your wish!")

            if candle_blown:
                st.snow()
                st.markdown("""
                    <div class='letter-card'>
                        <h2 style='font-size: 2rem; font-weight: bold;'>🎉 MY ULTIMATE WISH FOR YOU 🎉</h2>
                        <p style='font-size: 1.2rem; font-weight: bold;'>
                        May you completely crush our Class 10 board exams, score top ranks, and secure everything you want!
                        </p>
                        <p style='font-size: 1.1rem;'>No matter where life takes us after school finishes, we remain brothers for life. Have an absolute blast today, Saksham! 🥂</p>
                    </div>
                """, unsafe_allow_html=True)
st.markdown("""

From your best friend,

Subhash Maurya ❤️

""", unsafe_allow_html=True)
