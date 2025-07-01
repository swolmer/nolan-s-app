import streamlit as st
from utils.loader import (
    get_random_affirmation,
    get_emergency_message,
    get_random_love_note,
    get_proof_item
)

st.set_page_config(page_title="Nolan’s Safe Space", page_icon="🌲", layout="centered")

trail_markers = [
    {
        "label": "💪 Boost Me",
        "content": lambda: st.success(get_random_affirmation()),
        "left": "24%", "top": "36%",
        "key": "marker_0"
    },
    {
        "label": "🏕️ Emergency Shelter",
        "content": lambda: st.info(get_emergency_message()),
        "left": "30%", "top": "48%",
        "key": "marker_1"
    },
    {
        "label": "📜 Mark Wins",
        "content": lambda: st.success(get_proof_item()),
        "left": "40%", "top": "63%",
        "key": "marker_2"
    },
    {
        "label": "💌 Love Letters from Sophie",
        "content": lambda: st.write(get_random_love_note()),
        "left": "56%", "top": "60%",
        "key": "marker_3"
    },
    {
        "label": "📸 Our Moments",
        "content": lambda: st.write("""
            • That hike where we got lost but kept laughing  
            • The night we stayed up talking with no lights  
            • Your birthday surprise  
            • The first time you said you felt safe with me  
            • Every time you look at me like I’m home  
        """),
        "left": "70%", "top": "45%",
        "key": "marker_4"
    },
    {
        "label": "🚰 Water & Rest",
        "content": lambda: st.write("""
            You don’t have to summit today, Nolan.\nTake your water, breathe deep, and rest.\nYou’re still on your path.
        """),
        "left": "82%", "top": "24%",
        "key": "marker_5"
    },
]

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
        </style>
        """,
        unsafe_allow_html=True
    )

if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    set_background("https://raw.githubusercontent.com/swolmer/nolan-s-app/main/assets/welcome_bg.png")

    st.markdown(
        """
        <div style="background:rgba(255,255,255,0.90); padding:2.5rem; border-radius:18px; text-align:center; max-width:750px; margin: 5rem auto 3rem auto; border: 1.5px solid #e6e6e6;">
        <h1 style="font-size:2.7rem; margin-bottom:0.5rem">🌄 Nolan’s Safe Space</h1>
        <p style="font-size:1.2rem;">
        Welcome to your safe space.<br>Take a moment to breathe.<br><br>
        Sophie made this for you — for the tough moments.<br>
        Because she loves you and wants to be here, even when she can't be.<br><br>
        <b>You are enough.</b><br>
        You are so much more than you can see right now.<br>
        <b>You are so loved.</b>
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("🧭 Enter Your Trail"):
        st.session_state.entered = True

else:
    set_background("https://raw.githubusercontent.com/swolmer/nolan-s-app/main/assets/map_scene.png")

    st.markdown(
        """
        <div style="height:750px; width:100%; max-width:1100px; margin:auto; position:relative;">
            <div style="position:absolute;top:1.8rem;left:0;right:0;z-index:2; text-align:center;">
                <h1 style="background:rgba(255,255,255,0.92);display:inline-block; border-radius:12px; padding:0.65em 2.3em 0.55em 2.3em; font-size:2.6rem; font-weight:800; color:#222; box-shadow:0 2px 15px 0 #0002;">
                🗺️ Choose a Trail Marker
                </h1>
                <div style="color:#444;font-size:1.17rem; background:rgba(255,255,255,0.74); margin:0.8rem auto 0.3rem auto; max-width:390px; border-radius:9px;">
                    Each post is here to guide you. Follow the trail!
                </div>
            </div>
            <div id="trail-posts" style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:5;">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for marker in trail_markers:
        key = marker["key"]
        st.markdown(
            f"""
            <div style="position:absolute; left:{marker['left']}; top:{marker['top']}; z-index:8; min-width:160px; text-align:center;">
                <button onclick="window.parent.postMessage('{key}', '*')"
                        style="background:rgba(255,255,255,0.95); border:2.2px solid #7c7045; box-shadow:0 2px 10px #aaa5; color:#272504; font-weight:700;
                        font-size:1.14rem; border-radius:11px; padding: 0.7em 1.6em 0.55em 1.6em; margin-bottom:0.2em; cursor:pointer;">
                    {marker['label']}
                </button>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.session_state.get(key, False):
            marker["content"]()

        st.markdown(
            f"""
            <script>
            window.addEventListener("message", (e) => {{
                if (e.data === "{key}") {{
                    window.location.hash = "#{key}";
                    window.parent.postMessage("streamlit:setComponentValue", "*");
                }}
            }});
            </script>
            """,
            unsafe_allow_html=True
        )

    # Instructions footer for mobile
    st.markdown(
        """
        <div style="position:fixed;bottom:14px;right:0;left:0;text-align:center;color:#4d4d4d; background:rgba(255,255,255,0.9);padding:10px 0; font-size:1rem;z-index:99; box-shadow:0 1.5px 7px #3332;">
        🌲 Tap a marker to view its message — then explore the whole trail!
        </div>
        """,
        unsafe_allow_html=True
    )
