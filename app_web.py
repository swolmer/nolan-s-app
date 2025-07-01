import streamlit as st
from utils.loader import (
    get_random_affirmation,
    get_emergency_message,
    get_random_love_note,
    get_proof_item
)

st.set_page_config(page_title="Nolan’s Safe Space", page_icon="🌲", layout="wide")

# Background styling
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
            border-radius: 12px;
            max-width: 700px;
            margin: 4rem auto;
        }}
        button {{
            font-size: 16px !important;
            margin-bottom: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Entrance state
if "entered" not in st.session_state:
    st.session_state.entered = False

# 🌼 WELCOME SCREEN
if not st.session_state.entered:
    set_background("https://raw.githubusercontent.com/swolmer/nolan-s-app/main/welcome_bg.png")

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

# 🧭 TRAIL MAP PAGE
else:
    set_background("https://raw.githubusercontent.com/swolmer/nolan-s-app/main/topo_map.png")

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("🗺️ Choose Your Trail Marker")
    st.markdown("Each stop is here for you. Click where you need to go.")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("💪 Boost Me"):
            st.success(get_random_affirmation())

        if st.button("📜 Mark Wins"):
            st.success(get_proof_item())

    with col2:
        if st.button("🏕️ Emergency Shelter"):
            st.info(get_emergency_message())

        if st.button("📸 Our Moments"):
            st.write("""
            • That hike where we got lost but kept laughing  
            • The night we stayed up talking with no lights  
            • Your birthday surprise  
            • The first time you said you felt safe with me  
            • Every time you look at me like I’m home  
            """)

    with col3:
        if st.button("💌 Love Letters from Sophie"):
            try:
                st.write(get_random_love_note())
            except FileNotFoundError:
                st.warning("Sophie hasn't added letters yet!")

        if st.button("🚰 Water & Rest"):
            st.write("You don’t have to summit today, Nolan.\nTake your water, breathe deep, and rest.\nYou’re still on your path.")
