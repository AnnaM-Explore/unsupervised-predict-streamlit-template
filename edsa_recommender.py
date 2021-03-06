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
colfil = Image.open('resources/imgs/colfil.png')
col = Image.open('resources/imgs/Col.png')
confil = Image.open('resources/imgs/confil.png')
chewie = Image.open('resources/imgs/chewie.jpg')
cumulative = Image.open('resources/imgs/cumgenre.png')
dc = Image.open('resources/imgs/dc.png')
eda1 = Image.open('resources/imgs/eda1.png')
eda2 = Image.open('resources/imgs/eda2.png')
eda3 = Image.open('resources/imgs/eda3.png')
eda4 = Image.open('resources/imgs/eda4.png')
genre = Image.open('resources/imgs/genre.png')
how = Image.open('resources/imgs/how2.jpg')
katlego = Image.open('resources/imgs/katlego.jpg')
lehlogonolo = Image.open('resources/imgs/lehlogonolo1.jpg')
marvel = Image.open('resources/imgs/marvel.png')
movie = Image.open('resources/imgs/movie_icon.jpg')
pack = Image.open('resources/imgs/pack.jpg')
pop = Image.open('resources/imgs/popm.png')
pred = Image.open('resources/imgs/pred.png')
rating = Image.open('resources/imgs/ratingyear.png')
recent = Image.open('resources/imgs/recent.png')
reel = Image.open('resources/imgs/reel.png')
sim = Image.open('resources/imgs/sim.jpg')
shella = Image.open('resources/imgs/shella.jpg')
tags = Image.open('resources/imgs/tags.png')

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

# Load raw data
raw = pd.read_csv("resources/data/movies.csv")

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","How It Works","Recommender System","Solution Overview", "Data", "EDA", "About Us"]

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
        st.title("Movie Recommender System :sparkles: ")
        st.image(movie, width=630)
        st.image(marvel, width=850, caption="Whether you're a Marvel fan...")
        st.image(dc, width=850, caption="A DC fan ...")
        st.image(recent, width=850, caption="Or something inbetween...")
        st.markdown("We've got the best movie recommendation for you!")
        st.info(" Movie quote of the day")
        st.image(chewie, width=600)
        st.markdown("Translation: All we have to decide is what do with the time that is given.")

    if page_selection == "How It Works":
        st.title("How the app works")
        st.write("Our app uses one of the best Machine Learning algorithms to search our regularly updated database of movies and either recommends a similar to the ones the user likes or recommends movies based on their popularity and ratings so that the user never runs out of movies to watch.")
        st.image(pack, width=800)
        st.subheader("How to get a recommendation")
        st.write("1. Choose an algorithm")
        st.write("2. Choose your first favourite movie")
        st.write("3. Choose your second favourite movie")
        st.write("4. Choose your third favourite movie")
        st.write("5. Click on the recommend button")
        st.image(pop, width=550)
        st.info("Now you're all set. Let's make some recommendations!")


    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Our model works on both collaborative-based filtering and content-based filtering.")
        st.image(col, width=700)
        st.subheader("Collaborative Filtering")
        st.write(" * Matches users to people with similar tastes. Users who have similar tastes are put in a “basket” algorithmic-ally,  and recommendations are given based on what these users like on a whole. There are 3 approaches to this :  user-user collaborative filtering, item-item collaborative filtering and matrix factorization.")
        st.write("The prediction Pu,i is given by:")
        st.image(pred, width=400)
        st.write("* - Pu,i is the prediction of an item")
        st.write("* - rv,i is the rating given by a user v to a movie i")
        st.write("* - Su,v is the similarity between users")
        st.write("This algorithm is quite time consuming as it involves calculating the similarity for each user and then calculating prediction for each similarity score. One way of handling this problem is to select only a few users (neighbors) instead of all to make predictions, i.e. instead of making predictions for all similarity values, we choose only few similarity values. There are various ways to select the neighbors:")
        st.write("* - Select a threshold similarity and choose all the users above that value")
        st.write("* - Randomly select the users")
        st.write("* - Arrange the neighbors in descending order of their similarity value and choose top-N users")
        st.write("* - Use clustering for choosing neighbors")
        st.subheader("Content-based Filtering")
        st.write("* Uses a series of discrete characteristics of an item in order to recommend additional items with similar properties. Content-based filtering methods are totally based on a description of the item and a profile of the user’s preferences. It recommends items based on user’s past preferences.")
        st.write("* The content-based filtering algorithm finds the cosine of the angle between the profile vector and item vector, i.e. cosine similarity. Suppose A is the profile vector and B is the item vector, then the similarity between them can be calculated as:")
        st.image(sim)
        st.write("* Based on the cosine value, which ranges between -1 to 1, the movies are arranged in descending order and one of the two below approaches is used for recommendations:")
        st.write("* - Top-n approach: where the top n movies are recommended")
        st.write("* - Rating scale approach: Where a threshold is set and all the movies above that threshold are recommended")


    if page_selection == "Data":
        st.title("Raw Data")
        st.write("The raw data that was used to make this app possible")
        st.table(raw.head(10))
        st.write("There are 100004 rows and 3 columns")
    
    if page_selection == "EDA":
        st.title("Exploratory Data Analysis")
        st.write("The EDA that was done on the raw data provided for this app.")
        if st.checkbox('Ratings Per Class'):
            st.image(eda1)
        if st.checkbox('Most Popular Genre'):
            st.image(eda2, width=850)
        if st.checkbox('Top 10 Users'):
            st.image(eda3, width=800)
        if st.checkbox('Wordcloud of Movie Titles'):
            st.image(eda4, width=800)
        if st.checkbox('Number of Movies Rated Each Year'):
            st.image(rating, width=700)
        if st.checkbox('Wordcloud of Genres'):
            st.image(genre, width=700)
        if st.checkbox('Wordcloud of Movie Tags'):
            st.image(tags, width=700)
        if st.checkbox('Cumulative Number of Movies per Genre per Year'):
            st.image(cumulative, width=700)

    if page_selection == "About Us":
        st.image(banner, width=700)
        st.markdown("Meet the brains behind the operations! :construction_worker:")
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

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
