# InitialExtractor.py
# Streamlit UI: Extract initials from a full name

import streamlit as st

st.set_page_config(
    page_title="Initial Extractor",
    page_icon="🔤",
    layout="centered"
)

st.title("🔤 Initial Extractor")
st.markdown("Enter a full name and instantly get its initials (upper-case).")

name = st.text_input("Full Name:", placeholder="e.g., Ada Lovelace")

if name:
    initials = ".".join(part[0].upper() for part in name.strip().split() if part) + "."
    st.subheader("Initials")
    st.code(initials, language="text")
else:
    st.info("Start typing to see the initials here.")