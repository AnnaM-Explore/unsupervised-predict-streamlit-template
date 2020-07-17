"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# for displaying images
from PIL import Image
anna = Image.open('resources/imgs/Anna.png')
banner = Image.open('resources/imgs/banner.jpg')
chewie = Image.open('resources/imgs/chewie.jpg')
dc = Image.open('resources/imgs/dc.png')
marvel = Image.open('resources/imgs/marvel.png')
recent = Image.open('resources/imgs/recent.png')

# Add background colors
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","How it works","Recommender System", "Top 10 Recommendations","Solution Overview", "About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Home":
        st.title("Movie Recommender System")
        st.subheader("Welcome! :smile:")
        #st.markdown("Whether you are a Marvel fan...")
        st.image(marvel, width=850, caption="Whether you are a Marvel fan...")
        #st.write("A DC fan ...")
        st.image(dc, width=850, caption="A DC fan ...")
        #st.markdown("Or something inbetween")
        st.image(recent, width=850, caption="Or something inbetween...")
        st.markdown("We've got the best movie recommendation for you!")
        st.info(" Movie quote of the day")
        st.image(chewie, width=600)
        st.markdown("Translation: All we have to decide is what do with the time that is given.")

    
    if page_selection == "Top 10 Recommendations":
        st.title("Top movie recommendations")
        st.write("Some decription")
        st.write("Maybe add a funtion to return a certain number of movie recommendations?")
        st.write("Add button with top n function")

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    if page_selection == "About Us":
        #st.title("Our Team")
        st.image(banner, width=750)
        st.info("Meet the brains behind the operations!")
        st.info("Anna Modjadji")
        st.image(anna, width=250)
        st.markdown("some description here")
        st.markdown("Github: https://github.com/AnnaM-Explore")
        st.info("Katlego Mokgobu")
        st.markdown("picture goes here")
        st.markdown("some description here")
        st.markdown("some contact detail here")
        st.info("Lehlogonolo Mokwana")
        st.markdown("picture goes here")
        st.markdown("some description here")
        st.markdown("some contact detail here")
        st.info("Shella Lekalakala")
        st.markdown("picture goes here")
        st.markdown("some description here")
        st.markdown("some contact detail here")
        st.info("Trevas Elliott")
        st.markdown("picture goes here")
        st.markdown("some description here")
        st.markdown("some contact detail here")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
