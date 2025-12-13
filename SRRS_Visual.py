import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import os
import warnings
warnings.filterwarnings('ignore')


# Load cleaned file WITH clusters
df_clean = pd.read_csv("cleaned_with_clusters.csv")

# Load saved models
encoder = pickle.load(open("encoder.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
kmeans = pickle.load(open("kmeans_model.pkl", "rb"))

st.set_page_config(page_title="Swiggy Restaurant Recommendation System", page_icon=":bar_chart:", 
                   layout="wide")

st.title(":fork_and_knife: Swiggy Restaurant Recommendation System")

st.markdown('<style>div.block-container[padding-top:1rem;}</style>', unsafe_allow_html=True)

#City side bar
city = st.sidebar.multiselect("Select your city", df_clean['city'].unique())
if not city:
    df2 = df_clean.copy()

else:
    df2 = df_clean[df_clean['city'].isin(city)]

#Area side bar
Area = st.sidebar.multiselect("Select area", df2['Area'].unique())
if not Area:
    df3 = df2.copy()
else:
    df3 = df2[df2['Area'].isin(Area)]