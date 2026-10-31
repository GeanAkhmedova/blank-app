import streamlit as st

st.write("Well, hello there!")

@st.cache_data
def load_data():
    df = pd.read_csv("data/movies_genres_summary.csv")
    return df

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
