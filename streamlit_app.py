import streamlit as st
import pandas as pd

@st.cache_data
def load_cities(city_file):
    df = pd.read_csv(city_file)
    return df

st.title("GIS Demo App")
st.header("A simple demonstration that displays world cities using Streamlit's basic map function.")
st.markdown('''
World Cities Database is a comprehensive, up-to-date collection of global cities and towns maintained by Simple Maps (https://simplemaps.com/data/world-cities). 
It is built using trusted sources including the NGIA, US Geological Survey, US Census Bureau, and NASA.            
            ''')
cities=load_cities("data/worldcities.csv")
st.map(cities, latitude="lat", longitude="lng")
