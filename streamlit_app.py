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


st.write("Well, hello there!")

fandom_list = ['C', 'B', 'A', 'Twilight Series - Stephenie Meyer', 'A Knight of the Seven Kingdoms (TV)', 'Adventure Time']
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

full_tags =['Romance', 'First Time', 'English Season/Series 01', 'Truth Spells', '2Good2BTrue', 'Magic Revealed', 'Canon-Typical Violence', 'canon-typical behaviour', 'canon events', 'Blood\r\nand Injury', 'Drama & Romance', 'Canon Divergence - Ashford Tourney,\r\nEnemies to Lovers', 'Falling In Love', 'Angst with a Happy Ending,\r\nComplicated Relationships', 'unhealthy relationship dynamics', 'Obsession,\r\nFirst Kiss', 'Dragon Dreamers & Dragon Dreams (A Song of Ice and Fire),\r\nExplicit Sexual Content', 'Sexual Tension', 'Hand Jobs', 'Size Difference,\r\nBlow Jobs', 'Top Dunk | Duncan the Tall (A Song of Ice and Fire)', 'Bottom\r\nAerion Targaryen (Son of Maekar I)', 'Inexperienced Duncan the Tall,\r\nBlood Kink', 'Scar Kink', 'Jealousy', 'Slow Burn', 'Height difference,\r\n\r\nHurt/Comfort', 'Political Intrigue', 'Internal Conflict', 'Mutual Pining', 'Self-\r\nWorth Issues', 'Emotional Manipulation', 'Class Difference', 'Morally\r\n\r\nAmbiguous Character', 'Wet Cat Prince Meets Golden Retriever Knight,\r\nAerion Targaryen’s Terrible No Good Very Bad Personality', 'Duncan the\r\nTall and Morally Conflicted', 'Beta’d We Live Like Baelor Breakspear (In\r\nThis Fic At Least)', 'Author Apologizes For Making Up Places But\r\nNeeded A Few Lesser Lords To Bully For The Plot', 'POV Alternating,\r\nOther Additional Tags to Be Added', 'Male-Female Friendship', 'Past Relationship(s)', 'Complicated\r\nRelationships', 'Set before Islands', 'After Jelly Beans Have Power,\r\nGuilt', 'Fatherhood\r\nFamily Feels\r\nDysfunctional Family\r\nCharacter Study\r\nAngst\r\nDeveloping Friendships']
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
    #st.write("Nothing here yet :(") 
    #if word_min == 0:
        #st.write("poop")
        
    res = df
    for i in range(5,8):
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
        right.markdown("Link: ", res.loc[i, "Link"])
        st.write("Summarry: ", res.loc[i,"Summary"])
    


