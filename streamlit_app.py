import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
