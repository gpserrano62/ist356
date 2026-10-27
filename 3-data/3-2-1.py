import streamlit as st
import pandas as pd
import numpy as np

url = "https://github.com/mafudge/datasets/blob/master/delimited/webtraffic.log"

data = pd.read.csv(url, sep=" ", skiprows=3) 

st.dataframe(data)