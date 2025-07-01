import streamlit as st
import random
from utils.loader import (
    get_random_affirmation,
    get_emergency_message,
    get_random_love_note,
    get_proof_item
)

st.set_page_config(page_title="Nolan’s Safe Space", page_icon="🌿", layout="centered")

st.title("🌄 Nolan’s Safe Space")

with st.expander("❤️ Welcome Message", expanded=True):
    st.write("""
    Welcome to your safe space.  
    Take a moment to breathe.  

    Sophie made this for you — for the tough moments.  
    Because she loves you and wants to be here, even when she can't be.  

    You are enough.  
    You are so much more than you can see right now.  
    You are so loved.
    """)

st.markdown("---")

# Buttons for each post
col1, col2 = st.columns(2)

with col1:
    if st.button("💪 Boost Me"):
        st.success(get_random_affirmation())

    if st.button("🏕️ Emergency Shelter"):
        st.info(get_emergency_message())

    if st.button("📜 Mark Wins"):
        st.success(get_proof_item())

with col2:
    if st.button("💌 Love Letters from Sophie"):
        try:
            st.write(get_random_love_note())
        except FileNotFoundError:
            st.warning("Sophie hasn't added letters yet!")

    if st.button("📸 Our Moments"):
        st.write("""
        • That hike where we got lost but kept laughing  
        • The night we stayed up talking with no lights  
        • Your birthday surprise  
        • The first time you said you felt safe with me  
        • Every time you look at me like I’m home  
        """)

    if st.button("🚰 Water & Rest"):
        st.write("You don’t have to summit today, Nolan.\nTake your water, breathe deep, and rest.\nYou’re still on your path.")
