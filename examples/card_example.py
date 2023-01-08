import streamlit as st

from ogarantia_streamlit_card import card

st.title("Streamlit Card - example")

res = card(
    title="Streamlit Card",
    text="This is a test card",
    image="https://get.ogre.run/images/ogarantia_logoBlue.png"
    url="https://github.com/Ogarantia/st-card"
)

st.write(res)
