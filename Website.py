import pickle
import streamlit as st
import requests
import time
import numpy as np
import pandas as pd
from time import sleep


st.set_page_config(layout="wide")

movies_data=pd.read_csv("modified_dataset.csv")
similarity_matrix=np.load('similarity_matrix.npy',allow_pickle=True)
st.markdown("<h1 style='text-align: center;'>Movies Recommendation System</h1>", unsafe_allow_html=True)



def get_poster(movie_id, retries=5):
    base_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=fe8f2f85a68fa7ca17c0c58c19823b90&language=en-US'
    for attempt in range(retries):
        try:
            response = requests.get(base_url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return f'https://image.tmdb.org/t/p/w500{poster_path}'  # Construct the full URL
            else:
                return None  # Indicate no poster available
        except requests.exceptions.RequestException as e:
            sleep(2 ** (attempt + 1))  # Exponential backoff for retries
            print(attempt)
            print(f"Error retrieving poster for movie ID {movie_id}: {e}")
    return None  # No poster after retries


def top5(given):
    l=[]
    m=[]
    movie_index=movies_data[movies_data['title']==given].index[0]
    estimated=sorted(list(enumerate(similarity_matrix[movie_index])),reverse=True,key=lambda x:x[1])
    for i in estimated[1:6]:
        k=movies_data[movies_data['number']==i[0]]
        n=k['id'].values[0]
        path=get_poster(n)
        m.append(path)
        l.append(k['title'].values[0])
    return l,m
st.subheader("Select one or more movies from the dropbox")
x=st.multiselect('Due to some reasons this website fetches posters for non jio users only',movies_data['title'])
c1, c2 = st.columns([9,1])
p=0
with c1:
    pass
with c2:
    if st.button("Recommend"):
        with st.spinner("LOADING....."):
            time.sleep(5)
        p=1
if p==1:
    co0,co1,co2,co3,co4,co5=st.columns(6,gap='small')
    for j in x:
        y,z=top5(j)
        with co0:
            f=movies_data[movies_data['title']==j]['id'].values[0]
            if f=="failed":
                st.write(f' Top 5 recommendations of {j}:')
            else:
                given=get_poster(f)
                st.write(f' Top 5 recommendations of')
                st.image(given)
        with co1:
            if z[0]=="failed":
                st.write(y[0])
            else:    
                st.write(y[0])
                st.image(z[0])
        with co2:    
            if z[1]=="failed":
                st.write(y[1])
            else:    
                st.write(y[1])
                st.image(z[1])
        with co3:    
            if z[2]=="failed":
                st.write(y[2])
            else:    
                st.write(y[2])
                st.image(z[2])
        with co4:    
            if z[3]=="failed":
                st.write(y[3])
            else:    
                st.write(y[3])
                st.image(z[3])
        with co5:    
            if z[4]=="failed":
                st.write(y[4])
            else:    
                st.write(y[4])
                st.image(z[4])
    
