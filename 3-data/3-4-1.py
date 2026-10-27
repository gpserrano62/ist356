# imports 

import streamlit as st
import pandas as pd
import numpy as np 

from check_functions import clean_currency

# main code

checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')

# transformations

checks['total_amount_cleaned'] = checks['total amount of check'].apply(clean_currency)
checks['gratuity_cleaned'] = checks.apply(lambda row: clean_currency(row['gratuity']), axis = 1)

#engineer columns 
checks['price_per_item'] = checks['total_amount_cleaned'] / checks['total items on check']
checks['price_per_person'] = checks['total_amount_cleaned'] / checks['party size']
checks['items_per_item'] = checks['total items on check'] / checks['party size']
checks['tip_percentage'] = checks['gratuity_cleaned'] / checks['total_amount_cleaned']

#top 1% is 99 percentile 
top25_pctile_items_per_person = np.percentile(checks['items_per_person'], 75)
top25_pctile_price_per_person = np.percentile(checks['price_per_person'], 75)

#apply the kpi
checks ['customer_type'] = checks.apply(lambda row: detect_whale(
    row['items_per_person'],
    row['price_per_person'],
    top25_pctile_items_per_person,
    top25_pctile_price_per_person,
), axis =1)

st.write("### Check data")
st.write(f"75 percentile of item per person:{top25_pctile_items_per_person}")
st.write(f"75 percentile of price per person:{top25_pctile_price_per_person}")


customer_values = checls ['customer_type'].value_counts()

cols = st.columns(len(customer_values))
for i, (customer_type, count) in enumerate(customer_values.items()):
    cols[i].metric(label=customer_type, value= count)

st.dataframe(checks)


