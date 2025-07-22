# TextStatistics.py
# Streamlit UI: Count words, sentences, and characters in a paragraph

import streamlit as st
import re

st.set_page_config(
    page_title="Text Statistics",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Text Statistics")
st.markdown("Paste or type any paragraph below and instantly see its **word**, **sentence**, and **character** counts.")

text = st.text_area(
    label="Your Paragraph:",
    height=150,
    placeholder="Type or paste your text here..."
)

def compute_stats(txt: str):
    """Return word, sentence, and character counts."""
    chars = len(txt)
    words = len(txt.split()) if txt.strip() else 0
    # Split on '.', '!', or '?' followed by whitespace or end of string
    sentences = len(re.findall(r'[.!?]+(?:\s|$)', txt)) if txt.strip() else 0
    return words, sentences, chars

if text:
    words, sentences, chars = compute_stats(text)
    st.subheader("Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Words", words)
    col2.metric("Sentences", sentences)
    col3.metric("Characters", chars)
else:
    st.info("Enter text above to see its statistics here.")