import streamlit as st
from functions import *
    
# text contents defining the analytics for each graph and what i infer

st.markdown(
    body=
    """ 
    ### Language division in the marketing campaign
    > - Mandarin has majority of the marketing campaign with 40,255 advertisements made in various fields
    > - Spanish takes the second spot with 40,102 advertisements.
    """
)
draw_pie_chart_language(language_pie_chart_count)

st.markdown(
    body=
    """
    ### Marketing Campaign modes in proportion
    > - Marketing Campaigns made in the mode of Influencers (40,169) and Search (40,157) have been used in abundance.
    """
)
draw_pie_chart_campaign(campaign_type_pie_chart_count)

st.markdown(
    body=
    """
    ### Marketing Campaign Target audience by proportion
    > - Most marketing campaigns had majority of their audience as males, whose age group was in the range 18-24
    """
)
draw_pie_chart_target_audi(target_audience_pie_chart_count)

st.markdown(
    body=
    """
    ### Marketing Campaign channels used by different companies in proportion
    > - Most companies preferred their campaigns to be advertised by Email (33,599)
    """
)
draw_pie_chart_channel(channel_pie_chart_count)

st.markdown(
    body=
    """
    ### Channel wise division for every company
    """
)
draw_bar_chart_company_channel_wise(channel_list,company_list,df=df)

st.markdown(
    body=
    f"""
    ### Average Return on Investment (ROI) for each company
    """
)
draw_bar_chart_for_roi_company_wise(average_roi_company_wise)

st.markdown(
    body=
    """
    ### Average ROI based on duration of campaign
    """
)
draw_bar_chart_for_duration_wise_roi(average_roi_duration_wise)

st.markdown(
    body="""
    ### Average ROI based on Location of campaign
    """
)
draw_pie_chart_for_location_wise_roi(average_roi_location_wise)

draw_line_chart_for_company_wise_impressions(company_to_impression_list)
print(company_to_impression_list)