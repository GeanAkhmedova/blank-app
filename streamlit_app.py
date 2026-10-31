import altair as alt
import datetime
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("Ao3 test - Sheet1 (7).csv")
    return df
df = load_data()

res = df.copy()
r = df.shape[0]
w = df.shape[1]
for i in range(r):
  for j in range(w):
    res.iloc[i,j] = str(res.iloc[i,j]).replace(' \r',' ')
    res.iloc[i,j] = str(res.iloc[i,j]).replace('\r','')
    res.iloc[i,j] = str(res.iloc[i,j]).replace('\n',' ')
    #if df.iloc[i,j] == None:
      #df.iloc[i,j] = '0'
  res.loc[i,"Word Count"] = str(res.loc[i, "Word Count"]).replace(",","")
  #df.loc[i, "Word Count"] = int(df.loc[i, "Word Count"])


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

#full_tags = ['Romance', 'First Time', 'English Season/Series 01', 'Truth Spells', '2Good2BTrue', 'Magic Revealed', 'Canon-Typical Violence', 'canon-typical behaviour', 'canon events', 'Bloodand Injury', 'Drama & Romance', 'Canon Divergence - Ashford Tourney,Enemies to Lovers', 'Falling In Love', 'Angst with a Happy Ending,Complicated Relationships', 'unhealthy relationship dynamics', 'Obsession,First Kiss', 'Dragon Dreamers & Dragon Dreams (A Song of Ice and Fire),Explicit Sexual Content', 'Sexual Tension', 'Hand Jobs', 'Size Difference,Blow Jobs', 'Top Dunk | Duncan the Tall (A Song of Ice and Fire)', 'BottomAerion Targaryen (Son of Maekar I)', 'Inexperienced Duncan the Tall,Blood Kink', 'Scar Kink', 'Jealousy', 'Slow Burn', 'Height difference,Hurt/Comfort', 'Political Intrigue', 'Internal Conflict', 'Mutual Pining', 'Self-Worth Issues', 'Emotional Manipulation', 'Class Difference', 'MorallyAmbiguous Character', 'Wet Cat Prince Meets Golden Retriever Knight,Aerion Targaryen’s Terrible No Good Very Bad Personality', 'Duncan theTall and Morally Conflicted', 'Beta’d We Live Like Baelor Breakspear (InThis Fic At Least)', 'Author Apologizes For Making Up Places ButNeeded A Few Lesser Lords To Bully For The Plot', 'POV Alternating,Other Additional Tags to Be Added', 'Male-Female Friendship', 'Past Relationship(s)', 'ComplicatedRelationships', 'Set before Islands', 'After Jelly Beans Have Power,Guilt', 'FatherhoodFamily FeelsDysfunctional FamilyCharacter StudyAngstDeveloping Friendships']
full_tags = ['Romance', 'First Time', 'English Season/Series 01', 'Truth Spells', '2Good2BTrue', 'Magic Revealed', 'Canon-Typical Violence', 'canon-typical behaviour', 'canon events', 'Blood and Injury', 'Drama & Romance', 'Canon Divergence - Ashford Tourney', 'Enemies to Lovers', 'Falling In Love', 'Angst with a Happy Ending', 'Complicated Relationships', 'unhealthy relationship dynamics', 'Obsession', 'First Kiss', 'Dragon Dreamers & Dragon Dreams (A Song of Ice and Fire)', 'Explicit Sexual Content', 'Sexual Tension', 'Hand Jobs', 'Size Difference', 'Blow Jobs', 'Top Dunk | Duncan the Tall (A Song of Ice and Fire)', 'Bottom Aerion Targaryen (Son of Maekar I)', 'Inexperienced Duncan the Tall', 'Blood Kink', 'Scar Kink', 'Jealousy', 'Slow Burn', 'Height difference', ' Hurt/Comfort', 'Political Intrigue', 'Internal Conflict', 'Mutual Pining', 'Self- Worth Issues', 'Emotional Manipulation', 'Class Difference', 'Morally  Ambiguous Character', 'Wet Cat Prince Meets Golden Retriever Knight', 'Aerion Targaryen’s Terrible No Good Very Bad Personality', 'Duncan the Tall and Morally Conflicted', 'Beta’d We Live Like Baelor Breakspear (In This Fic At Least)', 'Author Apologizes For Making Up Places But Needed A Few Lesser Lords To Bully For The Plot', 'POV Alternating', 'Other Additional Tags to Be Added', 'Male-Female Friendship', 'Past Relationship(s)', 'Set before Islands', 'After Jelly Beans Have Power', 'Guilt', 'Fatherhood Family Feels Dysfunctional Family Character Study Angst Developing Friendships']
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

def contains_substring_ignore_case(main_string, substring):
    return substring.lower() in main_string.lower()
    
if st.button("Show search results", type="primary"):
    #st.write("Nothing here yet :(") 
    #if word_min == 0:
        #st.write("poop")
    #res = df
    r = df.shape[0]

    #filtering over fandoms
    Set = range(r)
    SetNew = []
    for word in u_fandoms:
        for i in Set:
            if contains_substring_ignore_case(res.loc[i,"Fandom"], word):
                SetNew.append(i)
        Set = SetNew.copy()
        SetNew = []

    #filtering over word count

    for i in Set:
        if float(res.loc[i, "Word Count"]) >= word_min:
            if word_max == 0:
                SetNew.append(i)
            if word_max > float(res.loc[i, "Word Count"]):
                SetNew.append(i)
    Set = SetNew.copy()
    SetNew = []
            

    #filtering over included tags
    for word in u_good_tags:
        for i in Set:
            if contains_substring_ignore_case(res.loc[i,"Tags"].replace(' ',''), word.replace(' ','')):
                SetNew.append(i)
        Set = SetNew.copy()
        SetNew = []

    #filtering over excluded tags
    for word in u_bad_tags:
        for i in Set:
            if contains_substring_ignore_case(res.loc[i,"Tags"].replace(' ',''), word.replace(' ','')) == False:
                SetNew.append(i)
        Set = SetNew.copy()
        SetNew = []

    

    
    #res = df
    for i in Set:
        #st.write(i)
        st.subheader(res.loc[i,'Title'])
        left, middle, right = st.columns([3,3,1], border=True)
        with left:
            #st.write("Rating: ", res.loc[i,"Rating"])
            st.write("Author: ",res.loc[i, "Author"])
            st.write("Fandom:", res.loc[i, "Fandom"])
            st.write("Words: ", res.loc[i, "Word Count"])
            st.write("Relationships: ", res.loc[i, "Relationships"])    
        #left.markdown("hubba hubba")
        middle.markdown(res.loc[i,"Tags"])
        right.markdown(res.loc[i, "Link"])
        st.write("Summarry: ", res.loc[i,"Summary"])
        


