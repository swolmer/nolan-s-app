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
            position: relative;
            width: 100%;
            min-height: 500px;
            height: 70vh;
            margin-top: 0rem;
        }}
        .marker-wrapper {{
            position: absolute;
            margin: 0;
            transition: transform 0.3s;
        }}
        .marker {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 12px;
            padding: 0.6rem;
            width: 140px;
            text-align: center;
            user-select: none;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
            backdrop-filter: blur(10px);
            opacity: 0;
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
            font-size: 0.85rem;
            font-weight: 600;
            color: #4B321D;
            margin-top: 0.3rem;
        }}
        .trail-instructions {{
            font-size: 1.1rem;
            font-weight: 500;
            background: rgba(255, 255, 255, 0.9);
            padding: 0.75rem 1.2rem;
            border-radius: 12px;
            max-width: 500px;
            margin: 0 auto 2rem auto;
            text-align: center;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .footer {{
            text-align: center;
            color: #555;
            margin-top: 2rem;
            font-size: 0.75rem;
        }}
        .trail-title {{
            font-size: 2.2rem;
            font-weight: 700;
            text-align: center;
            margin-top: 2.5rem;
            margin-bottom: 0.5rem;
            color: #222;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 12px;
            padding: 0.5rem 1.5rem;
            display: inline-block;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Session state: Has the user entered the trail?
if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    set_background(WELCOME_BG)

    # Welcome Card
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )

    # Entry Button
    if st.button("🧭 Enter Your Trail"):
        st.session_state.entered = True

else:
    set_background(TRAIL_BG)

    # Trail marker data
    markers = [
        ("Boost Me", get_random_affirmation, "Open Boost Me"),
        ("Emergency Shelter", get_emergency_message, "Open Emergency Shelter"),
        ("Mark Wins", get_proof_item, "Open Mark Wins"),
        ("Love Letters from Sophie", get_random_love_note, "Open Love Letters"),
        ("Our Moments", lambda: """• That hike where we got lost but kept laughing  
• The night we stayed up talking with no lights  
• Your birthday surprise  
• The first time you said you felt safe with me  
• Every time you look at me like I’m home""", "Open Our Moments"),
        ("Water & Rest", lambda: """You don’t have to summit today, Nolan.  
Take your water, breathe deep, and rest.  
You’re still on your path.""", "Open Water & Rester & Rest"),
    ]
    # Title & Instructions
    st.markdown(
        '<div class="trail-title">🗺️ Choose a Trail Marker — I’m With You Every Step</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="trail-instructions">
            Follow the path. Each stop is here to guide you.
        </div>
        """,
        unsafe_allow_html=True
    )

   st.markdown('<div class="trail-grid">', unsafe_allow_html=True)

    step_y = 100
    offset_x = 120

    for idx, (label, content_func, btn_label) in enumerate(markers):
        direction = -1 if idx % 2 == 0 else 1
        left = 50  # base center
        top = idx * step_y
        shift = direction * offset_x
        add_line = "show-line" if idx < len(markers) - 1 else ""

        # Use Streamlit's button, styled like a full marker
        if st.button(label, key=f"btn-{idx}"):
            try:
                result = content_func()
                st.success(result if isinstance(result, str) else str(result))
            except FileNotFoundError:
                st.warning("Sophie hasn't added letters yet!")

        # Then render the styled marker wrapper (used only for layout)
        st.markdown(
            f"""
            <style>
            #{f"btn-{idx}"} {{
                position: absolute;
                left: calc({left}% + {shift}px);
                top: {top}px;
                background: rgba(255, 255, 255, 0.85);
                border-radius: 12px;
                padding: 0.6rem;
                width: 130px;
                text-align: center;
                user-select: none;
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
                backdrop-filter: blur(10px);
                font-family: 'Inter', sans-serif;
                font-size: 0.9rem;
                font-weight: 600;
                color: #4B321D;
                border: none;
                z-index: 1;
                transition: transform 0.3s ease;
            }}
            #{f"btn-{idx}"}:hover {{
                transform: scale(1.05);
                background-color: #f5e8dd;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
