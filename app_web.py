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
        @import url('https://fonts.googleapis.com/css2?family=PT+Serif:wght@400;700&display=swap');

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
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
            backdrop-filter: blur(16px);
        }}
        .trail-grid {{
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4.5rem;
            margin-top: 2rem;
            margin-bottom: 3rem;
        }}
        .trail-grid::before {{
            content: "";
            position: absolute;
            top: 0;
            bottom: 0;
            width: 4px;
            background-image: linear-gradient(to bottom, #8B5C2A 40%, rgba(0,0,0,0) 0%);
            background-position: right;
            background-size: 1px 14px;
            background-repeat: repeat-y;
            z-index: 0;
        }}
        .marker {{
            background: rgba(255,255,255,0.85);
            border-radius: 12px;
            padding: 0.6rem 0.6rem;
            width: 130px;
            cursor: pointer;
            text-align: center;
            user-select: none;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            position: relative;
            font-size: 0.85rem;
            line-height: 1.3rem;
            backdrop-filter: blur(10px);
            z-index: 1;
            opacity: 0;
            animation: fadeIn 0.8s ease forwards;
            transition: transform 0.3s ease;
        }}
        .marker:hover {{
            transform: scale(1.05);
        }}
        .marker img {{
            width: 36px !important;
            margin-bottom: 0.25rem;
        }}
        .marker:nth-child(odd) {{
            transform: translateX(-120px);
        }}
        .marker:nth-child(even) {{
            transform: translateX(120px);
        }}
        .marker button, .marker button span {{
            font-size: 0.65rem !important;
            line-height: 1.1rem !important;
            padding: 0.3rem 0.6rem !important;
            background-color: #8B5C2A !important;
            color: white !important;
            border: 2px solid #5A3E1B !important;
            border-radius: 6px !important;
            font-weight: 600 !important;
            margin-top: 0.3rem !important;
            box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }}
        .marker button:hover {{
            background-color: #A06A36 !important;
            border-color: #6A4724 !important;
            transform: scale(0.97);
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
            background: rgba(255,255,255,0.85);
            border-radius: 12px;
            padding: 0.5rem 1.5rem;
            display: inline-block;
            box-shadow: 0 2px 12px rgba(0,0,0,0.04);
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

    if st.button("🧭 Enter Your Trail"):
        st.session_state.entered = True

else:
    set_background(TRAIL_BG)

    st.markdown(
        '<div style="text-align:center;"><div class="trail-title">🗺️ Choose a Trail Marker</div></div>',
        unsafe_allow_html=True
    )
    st.markdown("Follow the path. Each stop is here to guide you.")

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
You’re still on your path.""", "Open Water & Rest")
    ]

    st.markdown('<div class="trail-grid">', unsafe_allow_html=True)
    cols = st.columns(len(markers))  # Create columns for the markers
    for idx, (label, content_func, btn_label) in enumerate(markers):
        with cols[idx]:
            st.markdown("<br>" * idx, unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="marker">
                    <img src="{WOOD_POST}" width="60" />
                    <h3 style="margin-top:0.2rem;">{label}</h3>
                """,
                unsafe_allow_html=True
            )
            if st.button(btn_label, key=btn_label):
                try:
                    result = content_func()
                    if isinstance(result, str):
                        st.success(result)
                    else:
                        st.write(result)
                except FileNotFoundError:
                    st.warning("Sophie hasn't added letters yet!")
            st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="footer">🌲 Tap a marker to view its message — then explore the whole trail!</div>',
        unsafe_allow_html=True
    )
