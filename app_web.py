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
            background: rgba(255, 255, 255, 0.85);
            padding: 2rem 3rem;
            border-radius: 18px;
            max-width: 600px;
            margin: 5vh auto 2rem auto;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
            backdrop-filter: blur(8px);
        }}
        .trail-grid {{
            display: grid;
            grid-auto-flow: column;
            grid-auto-rows: 1fr;
            gap: 2.5rem;
            justify-content: center;
            align-items: start;
            margin-top: 4rem;
            margin-bottom: 4rem;
        }}
        .marker {{
            background: rgba(255,255,255,0.85);
            border-radius: 12px;
            padding: 1.2rem 1.5rem;
            width: 170px;
            cursor: pointer;
            text-align: center;
            user-select: none;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            position: relative;
        }}
        .marker img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 0.5rem;
        }}
        /* Diagonal effect: stagger each marker */
        .marker:nth-child(2n-1) {{ transform: translateY(0rem); }}
        .marker:nth-child(2) {{ transform: translateY(2rem); }}
        .marker:nth-child(3) {{ transform: translateY(4rem); }}
        .marker:nth-child(4) {{ transform: translateY(6rem); }}
        .marker:nth-child(5) {{ transform: translateY(8rem); }}
        .marker:nth-child(6) {{ transform: translateY(10rem); }}
        .dotted-line {{
            border-left: 3px dotted #8B5C2A;
            height: 80px;
            margin: 0 auto;
            width: 0;
        }}
        .footer {{
            text-align: center;
            color: #555;
            margin-top: 2rem;
            font-size: 0.9rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    set_background("assets/welcome_bg.png")

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
    set_background("assets/grand_teton_map.png")

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("🗺️ Choose a Trail Marker")
    st.markdown("Follow the path. Each stop is here to guide you.")
    st.markdown('</div>', unsafe_allow_html=True)

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

    for idx, (label, content_func, btn_label) in enumerate(markers, 1):
        st.markdown(
            f'''
            <div class="marker">
                <img src="assets/wood_post.png" width="60" />
                <h3 style="margin-top:0.2rem;">{label}</h3>
            ''',
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
        st.markdown('</div>', unsafe_allow_html=True)
        # Add a dotted line except after the last marker
        if idx < len(markers):
            st.markdown('<div class="dotted-line"></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">🌲 Tap a marker to view its message — then explore the whole trail!</div>', unsafe_allow_html=True)
