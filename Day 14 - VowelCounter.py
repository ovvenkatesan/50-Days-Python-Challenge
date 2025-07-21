# VowelCounter.py
import streamlit as st

def count_vowels(word):
    """Count vowels (case-insensitive) in a given word"""
    vowels = 'aeiou'
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

# Streamlit UI setup
st.title("Vowel Counter")
st.subheader("Count how many vowels are in a given word")

# Input with placeholder example
user_input = st.text_input(
    "Enter a word:",
    placeholder="e.g., Hello",
    key="word_input"
)

# Process input when user types
if user_input:
    vowel_count = count_vowels(user_input)
    
    # Display results with color-coded feedback
    st.subheader("Result:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Input Word", user_input)
    
    with col2:
        st.metric("Vowel Count", vowel_count)
    
    # Visual feedback
    if vowel_count == 0:
        st.warning("⚠️ No vowels found")
    else:
        vowels = [char for char in user_input if char.lower() in 'aeiou']
        st.success(f"Vowels detected: {', '.join(vowels)}")

# Add some styling and instructions
st.markdown("---")
st.markdown("**How it works:**")
st.markdown("1. Type any word in the input box above")
st.markdown("2. The app will count vowels (a, e, i, o, u)")
st.markdown("3. Both uppercase and lowercase vowels are counted")
st.markdown("4. See detailed results below the input field")

# Footer
st.markdown("---")
st.caption("Vowel Counter App • Made with Streamlit")