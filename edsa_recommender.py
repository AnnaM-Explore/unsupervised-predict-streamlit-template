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
banner1 = Image.open('resources/imgs/banner1.png')
banner2 = Image.open('resources/imgs/banner2.png')
batman = Image.open('resources/imgs/batman.jpg')
col = Image.open('resources/imgs/Col.png')
chewie = Image.open('resources/imgs/chewie.jpg')
dc = Image.open('resources/imgs/dc.png')
katlego = Image.open('resources/imgs/katlego.jpg')
how = Image.open('resources/imgs/how2.jpg')
lehlogonolo = Image.open('resources/imgs/lehlogonolo1.jpg')
marvel = Image.open('resources/imgs/marvel.png')
pack = Image.open('resources/imgs/pack.jpg')
pop = Image.open('resources/imgs/popm.png')
recent = Image.open('resources/imgs/recent.png')
reel = Image.open('resources/imgs/reel.png')
shella = Image.open('resources/imgs/shella.jpg')

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
    page_options = ["Home","How It Works","Recommender System","Solution Overview", "EDA", "About Us"]

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
        st.image(reel, width=550)
        st.image(marvel, width=850, caption="Whether you're a Marvel fan...")
        st.image(dc, width=850, caption="A DC fan ...")
        st.image(recent, width=850, caption="Or something inbetween...")
        st.markdown("We've got the best movie recommendation for you!")
        st.markdown("")
        st.info(" Movie quote of the day")
        st.image(chewie, width=600)
        st.markdown("Translation: All we have to decide is what do with the time that is given.")

    if page_selection == "How It Works":
        st.title("How the app works")
        #st.image(how, width=600)
        #st.write("Some picture here")
        st.write("Our app uses one of the best Machine Learning algorithms to search our regularly updated database of movies and either recommends a similar to the ones the user likes or recommends movies based on their popularity and ratings so that the user never runs out of movies to watch.")
        st.image(pack, width=800)

    if page_selection == "Top 10 Recommendations":
        st.title("Top movie recommendations")
        st.image(pop, width=400)
        st.write("Some decription")
        st.write("Add a funtion to return a certain number of movie recommendations based on a chosen movie")
        st.write("Add a button with function")

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Our model works on both collaborative-based filtering and content-based filtering.")
        st.image(col, width=700)
        st.write("*Collaborative Filtering*")
        st.write("*Builds a model from user’s past behavior (i.e. items purchased or searched by the user) as well as similar decisions made by other users. This model is then used to predict items (or ratings for items) that user may have an interest in.")
        st.write("*Content-based Filtering*")
        st.write("*Uses a series of discrete characteristics of an item in order to recommend additional items with similar properties. Content-based filtering methods are totally based on a description of the item and a profile of the user’s preferences. It recommends items based on user’s past preferences.")
        st.write("some pic here")
        st.write("Explain the top n function here")

    if page_selection == "EDA":
        st.title("Exploratory Data Analysis")
        st.write("Pictures of our notebook's EDA")

    if page_selection == "About Us":
        #st.title("Meet the brains behind the operations!")
        st.image(banner, width=700)
        st.markdown("Meet the brains behind the operations!")
        st.info("Anna Modjadji")
        st.image(anna, width=250)
        st.markdown("Data Science intern at Explore Data Science Academy")
        st.markdown("Github: https://github.com/AnnaM-Explore")
        st.info("Katlego Mokgobu")
        st.image(katlego, width=250)
        st.markdown("Data Science intern at Explore Data Science Academy")
        st.markdown("Github: https://github.com/mokgobukatlego-hub")
        st.info("Lehlogonolo Mokwana")
        st.image(lehlogonolo, width = 250)
        st.markdown("Data Science intern at Explore Data Science Academy")
        st.markdown("Github: https://github.com/LehlogonoloKAT")
        st.info("Shella Lekalakala")
        st.image(shella, width=250)
        st.markdown("Data Science intern at Explore Data Science Academy")
        st.markdown("Github: http://github.com/Shella9")
        st.info("Trevas Elliott")
        st.image(batman)
        st.markdown("Data Science intern at Explore Data Science Academy")
        st.markdown("some contact detail here")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
