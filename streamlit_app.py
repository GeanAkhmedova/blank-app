import altair as alt
import datetime
import pandas as pd
import streamlit as st
@st.cache_data
def load_data():
    df = pd.read_csv("Ao3 test - Sheet1 (1).csv")
    return df
df = load_data()

st.write("Well, hello there!")

fandom_list = ["F1", "F2", "F3"]
u_fandoms = st.multiselect(
    "Pick you fandoms!",
    fandom_list,
    select_all=False,
    )

options = ["Gen", "Teen", "Mature", "Explicit", "Unrated"]
selection = st.pills("Rating", options, selection_mode="multi")
#st.markdown(f"Your selected options: {selection}.")

col1, col2, col3 = st.columns(3)
with col1: 
    word_min = st.number_input(
    "Words min:", value=0
)
with col2: 
    word_max = st.number_input(
    "Words max:", value=0
)

full_tags = ["T1", "T2", "T3", "T4"]
u_good_tags = st.multiselect(
    "Include tags:",
    full_tags,
    select_all=False,
    )
u_bad_tags = st.multiselect(
    "Exclude tags:",
    full_tags,
    select_all=False,
    )

col1, col2 = st.columns(2)
with col1: 
    after = st.date_input("Published after", datetime.date(2026, 10, 30))
with col2: 
    before = st.date_input("Published before", datetime.date(2026, 10, 30))

sort_order = st.radio(
    "Sort by",
    ["Word count (longest first)", "Word count (shortest first)", "Date published (newest first)", "Date published (oldest first)"],
)

# st.write(df)
#st.text_input("Your name", key="name")

# You can access the value at any point with:
# st.session_state.name

if st.button("Show search results", type="primary"):
    st.write("Nothing here yet :(") 
    with st.sidebar:
        with st.echo():
            st.write("This code will be printed to the sidebar.")

        st.write("pppp")

