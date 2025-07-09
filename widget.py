import streamlit as st
import pandas as pd
import random
import datetime
df = pd.read_csv("movies.csv")

if st.button("데이터 조회"):
    st.datagram(df)

