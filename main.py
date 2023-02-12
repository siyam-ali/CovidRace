# CovidRace is a short program that utilizes streamlit and matplotlib to create a Racing Covid-19 Bar Chart
# that shows the increase in Cases in the top 10 most impacted countries. The dataset that we used contains data
# from January 2020 - May 2020, in the early stages of the pandemic. After running this program, a mp4 file
# will be generated in the same directory and streamlit will open a localhost webpage displaying the video.

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bar_chart_race as bcr
import seaborn as sb
import streamlit as st

covid_data = pd.read_csv('corona_dataset.csv')
top_countries = ['date', 'India', 'US', 'Brazil', 'France', 'Japan', 'Germany', 'Italy', 'Russia', 'China', 'Canada']

# Here we create a new variable that contains only the data from the top 10 countries we specified above.
top_cases = covid_data[top_countries]
top_cases.set_index('date', inplace=True)

# The cumulative sum function is for keeping track of the total cases in each country.
total_sum = top_cases.cumsum(axis=0)

# The below function allows us to create a mp4 file containing the "race" chart in the same directory.
bcr.bar_chart_race(df=total_sum, filename='animated_graph.mp4', figsize=(5,3), title='Top 10 Countries with the most COVID-19 Cases')

# And finally, st.video will open a localhost webpage displaying the racing bar chart of Covid Cases.
st.title('A real-time bar graph displaying the top countries with most COVID-19 cases from 01/2020 - 05/2020')
st.markdown('Note: The data displayed is used to analyze the early stages of the COVID-19 Pandemic.')
st.video('animated_graph.mp4')
st.subheader('Thank you for viewing my program!')



