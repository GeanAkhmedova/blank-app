import altair as alt
import pandas as pd
import streamlit as st

st.write("Well, hello there!")

fandom_list = ["F1", "F2", "F3"]
user_fandoms = st.multiselect(
    "Pick you fandoms!",
    fandom_list,
    select_all=False,
    )

@st.cache_data
def load_data():
    df = pd.read_csv("Ao3 test - Sheet1 (1).csv")
    return df
df = load_data()
st.write(df)
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name


clients = st.multiselect(
    "Select clients",
    ["Acme", "Globex", "Initech", "Umbrella", "Wayne"],
    select_all=False,
)

st.write("You selected:", clients)

options = ["Gen", "Teen", "Mature", "Explicit", "Unrated"]
selection = st.pills("Rating", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

col1, col2, col3, col4 = st.columns(4)

with col1: 
    fandom = st.multiselect(
    "Fandoms",
    ["Acme", "Globex", "Initech", "Umbrella", "Wayne"],
    select_all=False,
    )

with col2: 
    option4 = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
    )

with col3: 
    tags = st.multiselect(
        "Tags",
        ["Acme", "Globex", "Initech", "Umbrella", "Wayne"],
        select_all=False,
    )

with col4: 
    tags4 = st.multiselect(
        "Tags4",
        ["Acme", "Globex", "Initech", "Umbrella", "Wayne"],
        select_all=False,
    )
