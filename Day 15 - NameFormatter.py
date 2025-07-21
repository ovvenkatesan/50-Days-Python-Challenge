# NameFormatter.py
import streamlit as st

def format_name(full_name):
    """Format the name in different styles"""
    name_parts = full_name.strip().split()
    formats = {}
    
    # Original format
    formats["Original"] = full_name.strip()
    
    # Last, First format
    if len(name_parts) >= 2:
        formats["Last, First"] = f"{name_parts[-1]}, {' '.join(name_parts[:-1])}"
    
    # Last, First Middle format
    if len(name_parts) >= 3:
        formats["Last, First Middle"] = f"{name_parts[-1]}, {' '.join(name_parts[:-1])}"
    
    # First Middle Last format
    if len(name_parts) >= 3:
        formats["First Middle Last"] = ' '.join(name_parts)
    
    # Last, First Middle Initial format
    if len(name_parts) >= 3:
        middle_initials = ' '.join([f"{name[0]}." for name in name_parts[1:-1]])
        formats["Last, First M.I."] = f"{name_parts[-1]}, {name_parts[0]} {middle_initials}"
    
    # First M.I. Last format
    if len(name_parts) >= 3:
        middle_initials = ' '.join([f"{name[0]}." for name in name_parts[1:-1]])
        formats["First M.I. Last"] = f"{name_parts[0]} {middle_initials} {name_parts[-1]}"
    
    # UPPERCASE format
    formats["UPPERCASE"] = full_name.strip().upper()
    
    # lowercase format
    formats["lowercase"] = full_name.strip().lower()
    
    # Title Case format
    formats["Title Case"] = full_name.strip().title()
    
    return formats

# Streamlit UI
st.title("🔤 Name Formatter")
st.subheader("Transform names into different formats")
st.markdown("Enter a full name below to see it formatted in various styles")

# Input with example
name = st.text_input(
    "Enter full name:",
    placeholder="e.g., John Michael Smith",
    key="name_input"
)

if name:
    # Process the name
    formatted_names = format_name(name)
    name_parts = name.strip().split()
    
    # Display name structure analysis
    st.subheader("🔍 Name Structure")
    
    if len(name_parts) == 0:
        st.warning("Please enter a valid name")
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("First Name", name_parts[0])
        with col2:
            st.metric("Last Name", name_parts[-1] if len(name_parts) > 1 else "None")
        with col3:
            st.metric("Middle Parts", ", ".join(name_parts[1:-1]) if len(name_parts) > 2 else "None")
    
    # Display formatted names
    st.subheader("📝 Formatted Versions")
    
    # Two-column layout for formats
    col1, col2 = st.columns(2)
    
    with col1:
        for fmt in list(formatted_names.keys())[:4]:
            if fmt in formatted_names:
                st.code(f"{fmt}: {formatted_names[fmt]}", language="text")
    
    with col2:
        for fmt in list(formatted_names.keys())[4:]:
            if fmt in formatted_names:
                st.code(f"{fmt}: {formatted_names[fmt]}", language="text")
    
    # Show warning for insufficient name parts
    if len(name_parts) < 2:
        st.warning("⚠️ Add a last name for more formatting options")
    elif len(name_parts) < 3:
        st.info("ℹ️ Add middle names for additional formatting variations")

# Add examples and instructions
st.markdown("---")
st.markdown("**Examples to try:**")
st.markdown("- `John Michael Smith`  ")
st.markdown("- `emma watson`  ")
st.markdown("- `Dr. Jane Elizabeth Doe`  ")
st.markdown("- `ALEXANDER THE GREAT`  ")

st.markdown("**Features:**")
st.markdown("- Handles names with 1-5+ parts  ")
st.markdown("- Preserves original spacing and casing  ")
st.markdown("- Generates middle initials automatically  ")
st.markdown("- Shows name structure analysis  ")

# Footer
st.markdown("---")
st.caption("Name Formatter • Made with Streamlit")