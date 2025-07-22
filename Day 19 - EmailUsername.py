# EmailUsername.py
# Streamlit UI: Extract username from an email address

import streamlit as st

st.set_page_config(
    page_title="Email Username Extractor",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Username Extractor")
st.markdown("Enter an email address and instantly get the username (the part before the `@`).")

email = st.text_input(
    label="Email Address",
    placeholder="e.g., ada.lovelace@example.com"
)

if email:
    username = email.split("@")[0] if "@" in email else ""
    if username:
        st.subheader("Username")
        st.code(username, language="text")
    else:
        st.error("Please enter a valid email address containing '@'.")
else:
    st.info("Start typing to see the username here.")