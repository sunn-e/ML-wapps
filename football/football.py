import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

st.title("NBA Player Stats Explorer")

st.markdown("""
            Web App to scrape NBA stats data from [Here](https://www.basketball-reference.com/)
            """
            )

st.sidebar.header("User Input Features")
# the 2021 nba will happen in october,2021 so
# let's keep it till 2020 for now
selected_year = st.sidebar.selectbox("Year", list(
    reversed(range(1969, datetime.now().year))))

# everything is on the fly
# nothing is stored on the fly
# https://docs.streamlit.io/en/latest/caching.html


@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + \
        str(year) + "_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == "Age"].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(["Rk"], axis=1)
    return playerstats


playerstats = load_data(selected_year)
# playerstats
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect("Team", sorted_unique_team)
sele
unique_positions = ["C", "PF", "SF", "PG", "SG"]
# second and third arg is same so to give all options from all options as default(3rd arg)
selected_positions = st.sidebar.multiselect(
    "Position", unique_positions, unique_positions)

# noice filter condition with & from pandas
df_selected_team = playerstats[(playerstats.Tm.isin(
    selected_team)) & (playerstats.Pos.isin(selected_positions))]

st.header("Show player stats of selected team/s")
st.write("Data dimension" +
         str(df_selected_team.shape[0])+" Rows\n"+str(df_selected_team.shape[1])+" Columns")
st.dataframe(df_selected_team)


def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="plyersstats.csv">Download CSV File Yo</a>'
    return href


st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)
