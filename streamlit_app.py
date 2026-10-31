import streamlit as st

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

clients = st.multiselect(
    "Select clients",
    ["Acme", "Globex", "Initech", "Umbrella", "Wayne"],
    select_all=False,
)

st.write("You selected:", clients)

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

col1, col2, col3, col4 = st.columns(4)

with col1: fandom = st.multiselect(
    "Fandoms",
    ["Acme", "Globex", "Initech", "Umbrella", "Wayne"],
    select_all=False,
    )

with col2: option4 = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    )

with col3: tags = st.multiselect(
    "Fandoms",
    ["Acme", "Globex", "Initech", "Umbrella", "Wayne"],
    select_all=False,
)

with col4: tags4 = st.multiselect(
    "Fandoms",
    ["Acme", "Globex", "Initech", "Umbrella", "Wayne"],
    select_all=False,
)
