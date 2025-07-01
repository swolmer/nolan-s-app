import streamlit as st
from utils.loader import (
    get_random_affirmation,
    get_emergency_message,
    get_random_love_note,
    get_proof_item
)

st.set_page_config(page_title="Nolan’s Safe Space", page_icon="🌲", layout="centered")

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
            padding: 2rem 3rem;
            border-radius: 16px;
            text-align: center;
            max-width: 720px;
            margin: 4rem auto 2rem auto;
        }}
        .footer {{
            text-align: center;
            color: #555;
            margin-top: 2rem;
            font-size: 0.9rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

if "entered" not in st.session_state:
    st.session_state.entered = False

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

else:
    set_background("https://raw.githubusercontent.com/swolmer/nolan-s-app/main/assets/grand_teton_map.png")

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("🗺️ Choose a Trail Marker")
    st.markdown("Each post is here to guide you. Follow the trail!")
    st.markdown('</div>', unsafe_allow_html=True)

    markers = [
        ("💪 Boost Me", get_random_affirmation, "Open Boost Me"),
        ("🏕️ Emergency Shelter", get_emergency_message, "Open Emergency Shelter"),
        ("📜 Mark Wins", get_proof_item, "Open Mark Wins"),
        ("💌 Love Letters from Sophie", get_random_love_note, "Open Love Letters"),
        ("📸 Our Moments", lambda: """• That hike where we got lost but kept laughing  
• The night we stayed up talking with no lights  
• Your birthday surprise  
• The first time you said you felt safe with me  
• Every time you look at me like I’m home  """, "Open Our Moments"),
        ("🚰 Water & Rest", lambda: """You don’t have to summit today, Nolan.  
Take your water, breathe deep, and rest.  
You’re still on your path.""", "Open Water & Rest")
    ]

    # Add vertical spacing and buttons
    for label, content_func, btn_label in markers:
        st.markdown(f"### {label}")
        if st.button(btn_label):
            try:
                result = content_func()
                st.success(result) if isinstance(result, str) else st.write(result)
            except FileNotFoundError:
                st.warning("Sophie hasn't added letters yet!")
        st.markdown("<br>", unsafe_allow_html=True)  # spacing

    st.markdown('<div class="footer">🌲 Tap a marker to view its message — then explore the whole trail!</div>', unsafe_allow_html=True)
