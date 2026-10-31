import altair as alt
import datetime
import pandas as pd
import streamlit as st
@st.cache_data
def load_data():
    df = pd.read_csv("Ao3 test - Sheet1 (4).csv")
    return df
df = load_data()
r = df.shape[0]
full_tags = []
fandom_list = []
for i in range(r):
    unsep1 = df.loc[i,"Tags"]
    unsep2 = df.loc[i,"Fandom"]
    fic_tags = unsep1.split(', ')
    l1 = len(fic_tags)
    fic_fandoms = unsep2.split(', ')
    l2 = len(fic_fandoms)
    for j in range(l1):
        tag = fic_tags[j]
        if tag not in full_tags:
            full_tags.append(tag)
    for j in range(l2):
        tag = fic_fandoms[j]
        if tag not in fandom_list:
            fandom_list.append(tag)


st.write("Well, hello there!")

#fandom_list = ["F1", "F2", "F3"]
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

#full_tags = ["T1", "T2", "T3", "T4"]
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
    if word_min == 0:
        st.write("poop")
        
    res = df
    for i in range(3):
        st.subheader(res.loc[i,'Title'])
        left, middle, right = st.columns(3, border=True)
        with left:
            #st.write("Rating: ", res.loc[i,"Rating"])
            st.write("Author: ",res.loc[i, "Author"])
            st.write("Fandom:", res.loc[i, "Fandom"])
            st.write("Words: ", res.loc[i, "Word Count"])
            st.write("Relationships: ", res.loc[i, "Relationships"])    
        #left.markdown("hubba hubba")
        middle.markdown(res.loc[i,"Tags"])
        right.markdown("link to drive goes here")
        st.write("Summarry: ", res.loc[i,"Summary"])
    


