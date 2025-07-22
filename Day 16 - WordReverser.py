# WordReverser.py
# Streamlit UI: Reverse every individual word in a sentence

import streamlit as st

# --- Page configuration ---
st.set_page_config(
    page_title="Word Reverser",
    page_icon="🔁",
    layout="centered",
)

# --- Header ---
st.title("🔁 Word Reverser")
st.markdown("Enter any sentence and see each word reversed **in place**.")

# --- Text input ---
sentence = st.text_input(
    label="Type your sentence below:",
    placeholder="e.g., Hello World from Streamlit"
)

# --- Core logic & display ---
if sentence:
    reversed_words = [word[::-1] for word in sentence.split()]
    reversed_sentence = " ".join(reversed_words)

    st.subheader("Reversed Words")
    st.code(reversed_sentence, language="text")
else:
    st.info("Start typing to see the reversed output here.")