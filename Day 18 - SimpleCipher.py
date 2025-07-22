# SimpleCipher.py
# Streamlit UI: Caesar-style cipher that shifts each letter in a word by 1 position

import streamlit as st

st.set_page_config(
    page_title="Simple Cipher (+1 Shift)",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Simple Cipher")
st.markdown("Enter any word or sentence and instantly see every letter shifted **+1** position in the alphabet (wrapping Z → A).")

text = st.text_input("Your Text:", placeholder="e.g., Hello World")

def shift_one_letter(ch: str) -> str:
    """Shift a single alphabetic character by +1 (wrap-around)."""
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
    if 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + 1) % 26 + ord('A'))
    return ch  # Non-letters remain unchanged

if text:
    ciphered = ''.join(shift_one_letter(c) for c in text)
    st.subheader("Ciphered Text")
    st.code(ciphered, language="text")
else:
    st.info("Start typing to see the ciphered output here.")