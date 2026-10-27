import streamlit as st
import pandas as pd
import datetime

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls"

#imports the roster
roster = pd.read_csv(base + "roster.csv")

#import all polls
start_date = datetime.date(2024, 1, 8)
class_split = datetime.timedelta(days=7)

polls = []
for i in range(4):
    file_date = start_date + i * class_split
    file_date_string = datetime.datetime.strftime(file_date, "%Y-%m-%d")
    filename = f"poll_responses-{file_date_string}.csv"
    poll = pd.read_csv(base + filename)
    poll['poll_date'] = file_date
    poll['poll_filename'] = filename
    polls.append(poll)

polls_concat = pd.concat(polls) 

#merge roster with polls concat
polls_merged = pd.merge(roster, polls_concat, how='inner', left_on='netid', right_on='student_id')

#st.dataframe(roster)
#st.dataframe(polls_concat)
#st.dataframe(polls_merged)
# use pivot_table so roster is data is in the row and poll_date values are in the columns
# and use the values are the count of poll responses
poll_pivot = pd.pivot_table(index=['netid', 'name'], columns='poll_date', values='answer', aggfunc='count', fill_value=0)

#now melt the pivot table so that the poll_date is a column instead of an index
polls_melted = poll_pivot.reset_index().melt(id_vars=['netid', 'name'], var_name='poll_date', value_name='poll_date', value_name = 'response_count')

#student in row, count of responses > 0 in column
students_with_responses = stu

st.dataframe(poll_pivot)
