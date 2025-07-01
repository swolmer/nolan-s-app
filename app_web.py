import streamlit as st
from utils.loader import (
    get_random_affirmation,
    get_emergency_message,
    get_random_love_note,
    get_proof_item
)

st.set_page_config(page_title="Nolan’s Safe Space", page_icon="🌲", layout="centered")

# Use GitHub raw URLs for Streamlit Cloud compatibility
WELCOME_BG = "https://raw.githubusercontent.com/swolmer/nolan-s-app/main/assets/welcome_bg.png"
TRAIL_BG = "https://raw.githubusercontent.com/swolmer/nolan-s-app/main/assets/grand_teton_map.png"
WOOD_POST = "https://raw.githubusercontent.com/swolmer/nolan-s-app/main/assets/wood_post.png"
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=PT+Serif:wght@400;700&family=Inter:wght@400;600&display=swap');

        body {{
            background: #e6ecf0 !important;
        }}

        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'PT Serif', serif;
        }}

        .glass {{
            background: rgba(255, 255, 255, 0.90);
            padding: 2rem 3rem;
            border-radius: 18px;
            max-width: 600px;
            margin: 5vh auto 2rem auto;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.18);
            backdrop-filter: blur(16px);
        }}

        .trail-grid {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2.5rem;
            margin-top: 0;
            margin-bottom: 2rem;
            width: 100%;
        }}

        .marker-wrapper {{
            position: static;
            margin: 0;
            width: auto;
        }}

        .marker {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 12px;
            padding: 0.6rem;
            width: 130px;
            text-align: center;
            user-select: none;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
            backdrop-filter: blur(10px);
            opacity: 1;
            animation: fadeIn 0.8s ease forwards;
            transition: transform 0.3s ease;
            z-index: 1;
        }}

        .marker:hover {{
            transform: scale(1.05);
        }}

        .marker-icon {{
            width: 60px !important;
            margin-bottom: 0.25rem;
        }}

        .trail-label {{
            font-size: 0.75rem;
            font-weight: 600;
            color: #4B321D;
            margin-top: 0.3rem;
        }}

        .marker button,
        .marker button span,
        .stButton>button,
        .stButton>button span {{
            font-family: 'Inter', sans-serif !important;
            font-size: 0.8125rem !important;
            line-height: 1.1rem !important;
            padding: 0.3rem 0.6rem !important;
            background-color: #8B5C2A !important;
            color: white !important;
            border: 2px solid #5A3E1B !important;
            border-radius: 6px !important;
            font-weight: 600 !important;
            margin-top: 0.3rem !important;
            box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
            text-transform: none !important;
        }}

        .marker button:hover,
        .stButton>button:hover {{
            background-color: #A06A36 !important;
            border-color: #6A4724 !important;
            transform: scale(0.97);
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Session state to track if the user has "entered" the space
if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    set_background(WELCOME_BG)
    if st.button("🧭 Enter Your Trail"):
        st.session_state.entered = True
    st.markdown(
        '''
        <div class="glass">
            <h1>🌄 Nolan’s Safe Space</h1>
            <p>
            Welcome to your safe space.<br>
            Take a moment to breathe.<br><br>
            Sophie made this for you — for the tough moments.<br>
            Because she loves you and wants to be here, even when she can't be.<br><br>
            You are enough.<br>
            You are so much more than you can see right now.<br>
            You are so loved.
            </p>
        </div>
        ''',
        unsafe_allow_html=True
    )
else:
    set_background(TRAIL_BG)
    st.markdown('<div class="trail-title">🗺️ Choose a Trail Marker — I’m With You Every Step</div>', unsafe_allow_html=True)

    markers = [
        ("Boost Me", get_random_affirmation, "Open Boost Me"),
        ("Emergency Shelter", get_emergency_message, "Open Emergency Shelter"),
        ("Mark Wins", get_proof_item, "Open Mark Wins"),
        ("Love Letters from Sophie", get_random_love_note, "Open Love Letters"),
        ("Our Moments", lambda: """• That hike where we got lost but kept laughing  
• The night we stayed up talking with no lights  
• Your birthday surprise  
• The first time you said you felt safe with me  
• Every time you look at me like I’m home  """, "Open Our Moments"),
        ("Water & Rest", lambda: """You don’t have to summit today, Nolan.  
Take your water, breathe deep, and rest.  
You’re still on your path.""", "Open Water & Rester & Rest")
    ]

    st.markdown('<div class="trail-grid">', unsafe_allow_html=True)
    for idx, (label, content_func, btn_label) in enumerate(markers):
        st.markdown(
            f"""
            <div class="marker-wrapper">
                <div class="marker">
                    <img src="{WOOD_POST}" class="marker-icon" />
                    <div class="trail-label">{label}</div>
            """,
            unsafe_allow_html=True
        )
        if st.button(btn_label, key=f"btn-{idx}"):
            try:
                result = content_func()
                st.success(result if isinstance(result, str) else str(result))
            except FileNotFoundError:
                st.warning("Sophie hasn't added letters yet!")
        st.markdown("</div></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)