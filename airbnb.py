import pandas as pd
import pymongo
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

# Setting up page configuration

st.set_page_config(page_title= "Airbnb Data Visualization",
                   layout= "wide",
                   initial_sidebar_state= "expanded"                   
                  )

# Creating option menu in the side bar

with st.sidebar:
    selected = option_menu("Menu", ["Home","Overview","Explore"], 
                           icons=["house","graph-up-arrow","bar-chart-line"],
                           menu_icon= "menu-button-wide",
                           default_index=0,
                           styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#FF5A5F"},
                                   "nav-link-selected": {"background-color": "#FF5A5F"}}
                          )
# CREATING CONNECTION WITH MONGODB ATLAS AND RETRIEVING THE DATA

client = pymongo.MongoClient("mongodb+srv://ramyakrishnan:vasukrish@cluster0.mkkbqj1.mongodb.net/?retryWrites=true&w=majority")
db = client.sample_airbnb
col = db['listingsAndReviews']

# READING THE CLEANED DATAFRAME
df = pd.read_csv('Airbnb_data.csv')

# HOME PAGE

if selected == "Home":

    st.markdown("<h1 style='text-align: center; color: red;'>Airbnb Analysis</h1>",
            unsafe_allow_html=True)
    def setting_bg():
        st.markdown(f""" <style>.stApp {{
                    background:url("data:image/jpeg;base64,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");
                    background-size: cover}}
                </style>""", unsafe_allow_html=True)
    setting_bg()

    st.sidebar.markdown("#   ")
    st.sidebar.markdown("#   ")
    st.sidebar.markdown("## [TABLEAU DASHBORD](https://public.tableau.com/shared/JBTBNFJP7?:display_count=n&:origin=viz_share_link)")

    col1,col2 = st.columns(2,gap= 'medium')
    with col1:
        st.markdown("#   ")
        st.markdown("#   ")
        st.image("/Users/arul/Downloads/tittle.png")
        st.markdown("## :blue[Overview] : To analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. ")
    
    with col2:
        st.markdown("#   ")
        st.markdown("#   ")
        col2.image("/Users/arul/Downloads/home.jpeg")
        col2.markdown("## :blue[Domain] : Travel Industry, Property Management and Tourism")
        col2.markdown("## :blue[Technologies used] : Python, Pandas, Plotly, Streamlit, MongoDB")

# OVERVIEW PAGE
if selected == "Overview":
    tab1,tab2 = st.tabs(["$\huge 📝 RAW DATA $", "$\huge🚀 INSIGHTS $"])

    # RAW DATA TAB
    with tab1:
        # RAW DATA
        col1,col2 = st.columns(2)
        if col1.button("Click to view Raw data"):
            col1.write(col.find_one())
        # DATAFRAME FORMAT
        if col2.button("Click to view Dataframe"):
            col1.write(col.find_one())
            col2.write(df)

    # INSIGHTS TAB
    with tab2:
        # GETTING USER INPUTS
        country = st.sidebar.multiselect('Select a Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
        prop = st.sidebar.multiselect('Select Property_type',sorted(df.Property_type.unique()),sorted(df.Property_type.unique()))
        room = st.sidebar.multiselect('Select Room_type',sorted(df.Room_type.unique()),sorted(df.Room_type.unique()))
        price = st.slider('Select Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))
        
        # CONVERTING THE USER INPUT INTO QUERY
        query = f'Country in {country} & Room_type in {room} & Property_type in {prop} & Price >= {price[0]} & Price <= {price[1]}'
        
        # CREATING COLUMNS
        col1,col2 = st.columns(2,gap='medium')
        
        with col1:
            
            # TOP 10 PROPERTY TYPES BAR CHART
            df1 = df.query(query).groupby(["Property_type"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
            fig = px.bar(df1,
                         title='Top 10 Property Types',
                         x='Listings',
                         y='Property_type',
                         orientation='h',
                         color='Property_type',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True) 
        
            # TOP 10 HOSTS BAR CHART
            df2 = df.query(query).groupby(["Host_name"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
            fig = px.bar(df2,
                         title='Top 10 Hosts with Highest number of Listings',
                         x='Listings',
                         y='Host_name',
                         orientation='h',
                         color='Host_name',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig,use_container_width=True)
        
        with col2:
            
            # TOTAL LISTINGS IN EACH ROOM TYPES PIE CHART
            df1 = df.query(query).groupby(["Room_type"]).size().reset_index(name="counts")
            fig = px.pie(df1,
                         title='Total Listings in each Room_types',
                         names='Room_type',
                         values='counts',
                         color_discrete_sequence=px.colors.sequential.Rainbow
                        )
            fig.update_traces(textposition='outside', textinfo='value+label')
            st.plotly_chart(fig,use_container_width=True)
            
            # TOTAL LISTINGS BY COUNTRY CHOROPLETH MAP
            country_df = df.query(query).groupby(['Country'],as_index=False)['Name'].count().rename(columns={'Name' : 'Total_Listings'})
            fig = px.choropleth(country_df,
                                title='Total Listings in each Country',
                                locations='Country',
                                locationmode='country names',
                                color='Total_Listings',
                                color_continuous_scale=px.colors.sequential.Plasma
                               )
            st.plotly_chart(fig,use_container_width=True)

# EXPLORE PAGE
if selected == "Explore":
    st.markdown("## Explore more about the Airbnb data")
    
    # GETTING USER INPUTS
    country = st.sidebar.multiselect('Select a Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
    prop = st.sidebar.multiselect('Select Property_type',sorted(df.Property_type.unique()),sorted(df.Property_type.unique()))
    room = st.sidebar.multiselect('Select Room_type',sorted(df.Room_type.unique()),sorted(df.Room_type.unique()))
    price = st.slider('Select Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))
    
    # CONVERTING THE USER INPUT INTO QUERY
    query = f'Country in {country} & Room_type in {room} & Property_type in {prop} & Price >= {price[0]} & Price <= {price[1]}'
    
    # HEADING 1
    st.markdown("## Price Analysis")
    
    # CREATING COLUMNS
    col1,col2 = st.columns(2,gap='medium')
    
    with col1:
        
        # AVG PRICE BY ROOM TYPE BARCHART
        pr_df = df.query(query).groupby('Room_type',as_index=False)['Price'].mean().sort_values(by='Price')
        fig = px.bar(data_frame=pr_df,
                     x='Room_type',
                     y='Price',
                     color='Price',
                     title='Avg Price in each Room type'
                    )
        st.plotly_chart(fig,use_container_width=True)
        
        # HEADING 2
        st.markdown("## Availability Analysis")
        
        # AVAILABILITY BY ROOM TYPE BOX PLOT
        fig = px.box(data_frame=df.query(query),
                     x='Room_type',
                     y='Availability_365',
                     color='Room_type',
                     title='Availability by Room_type'
                    )
        st.plotly_chart(fig,use_container_width=True)
        
    with col2:
        
        # AVG PRICE IN COUNTRIES SCATTER_GEO
        country_df = df.query(query).groupby('Country',as_index=False)['Price'].mean()
        fig = px.scatter_geo(data_frame=country_df,
                                       locations='Country',
                                       color= 'Price', 
                                       hover_data=['Price'],
                                       locationmode='country names',
                                       size='Price',
                                       title= 'Avg Price in each Country',
                                       color_continuous_scale='agsunset'
                            )
        col2.plotly_chart(fig,use_container_width=True)
        
        # BLANK SPACE
        st.markdown("#   ")
        st.markdown("#   ")
        
        # AVG AVAILABILITY IN COUNTRIES SCATTER_GEO
        country_df = df.query(query).groupby('Country',as_index=False)['Availability_365'].mean()
        country_df.Availability_365 = country_df.Availability_365.astype(int)
        fig = px.scatter_geo(data_frame=country_df,
                                       locations='Country',
                                       color= 'Availability_365', 
                                       hover_data=['Availability_365'],
                                       locationmode='country names',
                                       size='Availability_365',
                                       title= 'Avg Availability in each Country',
                                       color_continuous_scale='agsunset'
                            )
        st.plotly_chart(fig,use_container_width=True)
        