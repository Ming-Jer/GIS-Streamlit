import streamlit as st
import pandas as pd

@st.cache_data
def load_cities(city_file):
    df = pd.read_csv(city_file)
    return df

st.title("GIS Demo App")
cities=load_cities("data/worldcities.csv")
st.map(cities, latitude="lat", longitude="lng")
