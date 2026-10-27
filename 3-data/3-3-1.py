import streamlit as st
import pandas as pd
import numpy as np 
import requests

# use requests to read this in as json data

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(url)
employee_data = response.json()

st.write(employee_data)

# loop over each key create a data frame and display
for key in employee_data.keys():
    st.write(f"Data for{key}:")
    df = pd.DataFrame(employee_data[key]) # employee_data[key] gets the val. ex: 'marketing' this is list 
    st.dataframe(df)

dfs = []
for key in employee_data.keys():
    df = pd.DataFrame(employee_data[key]) # employee_data[key] gets the val. ex: 'marketing' this is list 
    df['department'] = key 
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
st.write("Combined DataFrame")
st.dataframe(combined_df)

filename = "3-data/data/combined_employee_data.csv"
combined_df.to_json("combined_employee_data.json", orient="records", lines=False)
st.write(f"Combined DF saved to '{filename}' in JSON lines format")