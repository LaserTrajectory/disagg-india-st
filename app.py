import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.title("Disaggregation of Shares in Output-side Real GDP at Current Purchasing Power Parities")

st.subheader("By Aniruddh Bhaskaran (Ashoka University UG '23)")

# loading data from the csv files & renaming columns
df_c = pd.read_csv('https://raw.githubusercontent.com/LaserTrajectory/disagg-india/main/csh_c.csv')
df_c.rename(columns={'DATE':'Date', 'CSHCCPINA156NRUG':'csh_c'}, inplace=True)

df_g = pd.read_csv('https://raw.githubusercontent.com/LaserTrajectory/disagg-india/main/csh_g.csv')
df_g.rename(columns={'DATE':'Date', 'CSHGCPINA156NRUG':'csh_g'}, inplace=True)

df_i = pd.read_csv('https://raw.githubusercontent.com/LaserTrajectory/disagg-india/main/csh_i.csv')
df_i.rename(columns={'DATE':'Date', 'CSHICPINA156NRUG':'csh_i'}, inplace=True)

df_m = pd.read_csv('https://raw.githubusercontent.com/LaserTrajectory/disagg-india/main/csh_m.csv')
df_m.rename(columns={'DATE':'Date', 'CSHMCPINA156NRUG':'csh_m'}, inplace=True)

df_x = pd.read_csv('https://raw.githubusercontent.com/LaserTrajectory/disagg-india/main/csh_x.csv')
df_x.rename(columns={'DATE':'Date', 'CSHXCPINA156NRUG':'csh_x'}, inplace=True)

df_r = pd.read_csv('https://raw.githubusercontent.com/LaserTrajectory/disagg-india/main/csh_r.csv')
df_r.rename(columns={'DATE':'Date', 'CSHRCPINA156NRUG':'csh_r'}, inplace=True)

# display data
# st.dataframe(df_c)
# st.dataframe(df_g)
# st.dataframe(df_i)
# st.dataframe(df_x)
# st.dataframe(df_m)
# st.dataframe(df_r)

sel_com_c = df_c[["Date", "csh_c"]]
sel_com_g = df_g[["csh_g"]]
sel_com_i = df_i[["csh_i"]]
sel_com_x = df_x[["csh_x"]]
sel_com_m = df_m[["csh_m"]]
sel_com_r = df_r[["csh_r"]]

master = pd.DataFrame()

master = sel_com_c.copy()
master["csh_g"] = sel_com_g
master["csh_i"] = sel_com_i
master["csh_x"] = sel_com_x
master["csh_m"] = sel_com_m
master["csh_r"] = sel_com_r

st.text("Master data frame with component share data: ")

st.dataframe(master)

st.write("Source: https://www.rug.nl/ggdc/productivity/pwt/")

master.rename(columns={"csh_c": "Consumption", "csh_g": "Govt. Exp.", "csh_i": "Investment", "csh_x": "Exports", "csh_m": "Imports", "csh_r": "StatDiscrep"}, inplace=True)

fig_p = px.bar(master, x="Date", 
               y=["Exports", "Investment", "Govt. Exp.", "Consumption", "Imports", "StatDiscrep"], 
               title="India 1950-2019 GDP Disaggregation")
fig_p.update_layout(
    width=750,
    height=500
)
st.plotly_chart(fig_p)

st.write("""The graph above shows India's year-on-year disaggregation of output-side
            Real GDP into the five main components – Consumption, Investment, Government
            Expenditure, Imports and Exports. It also includes Statistical Discrepancy data
            so that the sum of the component values is as close to 1 as possible. This
            graph tells us the trend of each component relative to the years before it
            and can inform us on which components of GDP drive a particular country's 
            growth. For example, South Korea's economic growth has been historically driven by
            exports and investment. This can be seen in a similar [visualisation](https://public.tableau.com/profile/aniruddh.bhaskaran#!/vizhome/GDPExp_SideDisaggregationSouthKoreaAniBhaskaran/Disag) I made for South Korea's 
            Output-side GDP trends.""")

st.write("""We can see from the graph above that India's growth has been driven majorly by 
            two components – Consumption and Investment. These are the two components 
            that have grown the most relative to the other GDP components, as can
            be seen from the graph. As foreign investment has increased, the role of government
            expenditure has reduced in spurring GDP. However, in the last few years, 
            investment has reduced slightly and consumption has increased, along with
            exports, though the increase is negligible.""")

st.write("""Foreign investment is likely to fall further due to the pandemic. This graph shows us that
            historically, Indian growth has been driven heavily by foreign investment. Therefore
            we may infer that a post-pandemic growth strategy for India would include policies
            designed to ease the flow of capital and incentivise foreign investment.""")
