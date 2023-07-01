import numpy as np
import pandas as pd
import streamlit as st
import plotly as pl
import matplotlib.pyplot as plt
import seaborn as sb
from functions import *
# initialise streamlit and its contents
df = pd.read_csv("C:\\Users\\T ADITYA\\Desktop\\Desktop insider\\RNSIT\\6th sem subjects\\College internship\\Marketing campaign insights\\marketing_campaign_dataset.csv")
st.header('Marketing Campaign Analysis')
st.markdown(
    body=f"""
    - This dataset was taken from [kaggle.com](https://www.kaggle.com/datasets/manishabhatt22/marketing-campaign-performance-dataset)
    - It comprises of {len(df['Company'])} rows and 16 columns comprising of data related to the retention and effectiveness of the campaign
    - This dataset provides us the insights of marketing campaigns that were done across various cities in the united states.
    """
)
st.dataframe(df)
