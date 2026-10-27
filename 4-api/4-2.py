import json
import requests
import dotenv
import os
import streamlit as st
import pandas as pd
import json 


from extractors import extract_entities
dotenv.load_dotenv()

st.title("Entity Extraction with Cent API")
text=st.textarea("Enter text to extract entities from", "")
entities = extract_entities(text)
df = pd.json_normalize(entities)  # convert to a pandas dataframe
st.dataframe(df)
