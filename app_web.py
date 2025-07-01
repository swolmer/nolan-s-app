import streamlit as st
from utils.loader import (
    get_random_affirmation,
    get_emergency_message,
    get_random_love_note,
    get_proof_item
)

st.set_page_config(page_title="Nolan’s Safe Space", page_icon="🌲", layout="centered")

# 🌄 Background helper
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .glass {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            max-width: 720px;
            margin: 4rem auto 2rem auto;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Entrance screen state
if "entered" not in st.session_state:
    st.session_state.entered = False

# 🚪 Entrance screen
if not st.session_state.entered:
    set_background("https://raw.githubusercontent.com/swolmer/nolan-s-app/main/assets/welcome_bg.png")

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("🌄 Nolan’s Safe Space")
    st.markdown("""
    Welcome to your safe space.  
    Take a moment to breathe.  

    Sophie made this for you — for the tough moments.  
    Because she loves you and wants to be here, even when she can't be.  

    You are enough.  
    You are so much more than you can see right now.  
    You are so loved.
    """)
    if st.button("🧭 Enter Your Trail"):
        st.session_state.entered = True
    st.markdown('</div>', unsafe_allow_html=True)

# 🗺️ Trail Map screen
else:
    set_background("https://raw.githubusercontent.com/swolmer/nolan-s-app/main/assets/map_scene.png")

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("🗺️ Choose a Trail Marker")
    st.markdown("Follow the path. Each stop is here to guide you.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Trail Marker 1
    st.markdown("### 💪 Boost Me")
    if st.button("Open Boost Me"):
        st.success(get_random_affirmation())

    # Space between markers
    st.markdown(" ")

    # Trail Marker 2
    st.markdown("### 🏕️ Emergency Shelter")
    if st.button("Open Emergency Shelter"):
        st.info(get_emergency_message())

    st.markdown(" ")

    # Trail Marker 3
    st.markdown("### 📜 Mark Wins")
    if st.button("Open Mark Wins"):
        st.success(get_proof_item())

    st.markdown(" ")

    # Trail Marker 4
    st.markdown("### 💌 Love Letters from Sophie")
    if st.button("Open Love Letters"):
        try:
            st.write(get_random_love_note())
        except FileNotFoundError:
            st.warning("Sophie hasn't added letters yet!")

    st.markdown(" ")

    # Trail Marker 5
    st.markdown("### 📸 Our Moments")
    if st.button("Open Our Moments"):
        st.write("""
        • That hike where we got lost but kept laughing  
        • The night we stayed up talking with no lights  
        • Your birthday surprise  
        • The first time you said you felt safe with me  
        • Every time you look at me like I’m home  
        """)

    st.markdown(" ")

    # Trail Marker 6
    st.markdown("### 🚰 Water & Rest")
    if st.button("Open Water & Rest"):
        st.write("""
        You don’t have to summit today, Nolan.  
        Take your water, breathe deep, and rest.  
        You’re still on your path.
        """)
