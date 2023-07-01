import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as ex
import altair as alt


df = pd.read_csv("C:\\Users\\T ADITYA\\Desktop\\Desktop insider\\RNSIT\\6th sem subjects\\College internship\\Marketing campaign insights\\marketing_campaign_dataset.csv")
linguistic_df = df.copy()
languages_list = []
campaign_type_list = []
company_list = []
target_audience_list = []
customer_segment_list = []


languages_list = [x for x in list(df['Language'].unique())]
campaign_type_list = [x for x in list(df['Campaign_Type'].unique())]
company_list = [x for x in list(df['Company'].unique())]
target_audience_list = [x for x in list(df['Target_Audience'].unique())]
channel_list = [x for x in list(df['Channel_Used'].unique())]
customer_segment_list = [x for x in list(df['Customer_Segment'].unique())]
duration_list = [x for x in list(df['Duration'].unique())]
location_list = [x for x in list(df['Location'].unique())]


language_pie_chart_count = {}
campaign_type_pie_chart_count = {}
target_audience_pie_chart_count = {}
channel_pie_chart_count = {}
average_roi_company_wise = {'Company':[],'Average ROI':[]}
average_roi_duration_wise = {'Duration':[],'Average ROI':[]}
average_roi_location_wise = {}
company_to_impression_list ={}

for i in languages_list:
    language_pie_chart_count[i] = len(df[df['Language']==i] )
for i in campaign_type_list:
    campaign_type_pie_chart_count[i] = len(df[df['Campaign_Type']==i])
for i in target_audience_list:
    target_audience_pie_chart_count[i] = len(df[df['Target_Audience']==i])
for i in channel_list:
    channel_pie_chart_count[i] = len(df[df['Channel_Used']==i])            
for i in company_list:
    average_roi_company_wise['Company'].append(i)
    average_roi_company_wise['Average ROI'].append(sum(list(df[df['Company']==i]['ROI']))/len(df[df['Company']==i]))
for i in duration_list:
    average_roi_duration_wise['Duration'].append(i)
    average_roi_duration_wise['Average ROI'].append(sum(list(df[df['Duration']==i]['ROI']))/len(df[df['Duration']==i]))
for i in location_list:
    average_roi_location_wise[i] = sum(list(df[df['Location']==i]['ROI']))/len(df[df['Location']==i])

   
print(average_roi_duration_wise)
# define all the charts as functions by passing the respective list

def draw_pie_chart_language(lf:dict)->None: # language related pie chart
    fig = go.Figure(data=[go.Pie(labels=list(lf.keys()),
                                 pull=[0.1,0,0,0.2,0],
                                 textinfo='label+value',
                                 values=list(lf.values()))])
    fig.update_layout(
        autosize=True,
        width=400,
        height=400
    )
    st.plotly_chart(fig)

def draw_pie_chart_campaign(cf:dict)->None:
    fig = go.Figure(data=[go.Pie(labels=list(cf.keys()),
                                 pull=[0,0.2,0,0.1,0],
                                 textinfo='label+value',
                                 values=list(cf.values()))])
    fig.update_layout(
        autosize=True,
        width=400,
        height=400
    )
    st.plotly_chart(fig)

def draw_pie_chart_target_audi(tf:dict)->None:
    fig = go.Figure(data=[go.Pie(labels=list(tf.keys()),
                                 pull=[0.1,0,0,0,0],
                                 textinfo='label+value',
                                 values=list(tf.values()))])
    fig.update_layout(
        autosize=True,
        width=400,
        height=400
    )
    st.plotly_chart(fig)

def draw_pie_chart_channel(chf:dict)->None:
    fig = go.Figure(data=[go.Pie(labels=list(chf.keys()),
                                 pull=[0,0,0,0,0,0.1],
                                 textinfo='label+value',
                                 values=list(chf.values()))])
    fig.update_layout(
        autosize=True,
        width=400,
        height=400
    )
    st.plotly_chart(fig)
    
def draw_bar_chart_company_channel_wise(comp_chan:list,comp_list:list,df:pd.DataFrame)->None:
    option = st.selectbox(options=comp_chan,label='Choose channel for company wise analysis')
    if option:
        df_x = df[df['Channel_Used']==option]
        df_copy={'Company':[],'Value':[]}
        for i in comp_list:
            df_copy['Value'].append(len(df_x[df_x['Company']==i]))
            df_copy['Company'].append(i)
        st.bar_chart(data=df_copy,x='Company',y='Value',height=400,width=400)
        
def draw_bar_chart_for_duration_wise_roi(drf:dict)->None:
    st.bar_chart(data=drf,x='Duration',y='Average ROI')
def draw_bar_chart_for_roi_company_wise(crf:dict):
    st.bar_chart(data=crf,x='Company',y='Average ROI',height=400,width=400)
    
def draw_pie_chart_for_location_wise_roi(lroi:dict):
    fig = go.Figure(data=[go.Pie(labels=list(lroi.keys()),
                                 pull = [0,0,0,0.1,0],
                                 textinfo ='label+value',
                                values=list(lroi.values())
    )])
    fig.update_layout(
        autosize=True,
        height=400,
        width=400
    )
    st.plotly_chart(figure_or_data=fig)

def draw_line_chart_for_company_wise_impressions(company_to_impression_list:dict):
    option = st.selectbox(options=list(company_to_impression_list.keys()),label='Choose Company')
    if option:
        st.line_chart(data=company_to_impression_list[option])    

