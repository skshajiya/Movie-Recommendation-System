# Movie-Recommendation-System
Movie Recommendation System using IMDB Dataset with NLP and TF-IDF
* * *
# Table of Contents:
-[Overview](#Overview)

-[Dataset](#Dataset)

-[Techniques Used](#Techniiques-Used)

-[Implementation](#Implementation)

-[About project](#About-project)

-[DEMO](#DEMO)
* * *
# Overview:
This project aims to build a movie recommendation system using Natural Language Processing (NLP) techniques and TF-IDF (Term Frequency -Inverse Document Frequency) on the IMDB dataset. By analyzing movie descripitons, the system suggests similar movies to users based on their input.



# Dataset:
You can download the dataset [here](https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k?fbclid=IwAR2MpWrWpcw2QNCv_FZg2l0sjBh9xAvhrqtnZBO9K-QS6PHI1aHkdB6qLa0)
The IMDb dataset contains set of 10k top-rated TMDB movies till 26-July-2022., including titles, genres, descriptions, ratings, and more. The dataset is utilized to extract relevant features for building the recommendation system. 

* * *

# Techniques Used:

Natural Language Processing (NLP): NLP techniques are applied to analyze movie descriptions. Text preprocessing methods such as tokenization, stop word removal, and stemming are employed to extract meaningful features from the text data.

TF-IDF (Term Frequency-Inverse Document Frequency): TF-IDF is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents. It is utilized to represent each movie description as a numerical vector, capturing the significance of terms within the corpus.




Cosine Similarity: Cosine similarity is a metric used to measure the similarity between two vectors by computing the cosine of the angle between them. In this project, cosine similarity is applied to determine the similarity between movie descriptions and recommend similar movies based on user input.



* * *
# Implementation:

Data Preprocessing: Movie descriptions from the IMDb dataset are preprocessed using NLP techniques to extract relevant features and remove noise.

TF-IDF Vectorization: The preprocessed text data is transformed into the TF-IDF vectors, where each movie description is represented as a numerical vector.

Cosine Similarity Calculation: Cosine similarity scores are computed between the TF-IDF vectors of movie descriptions to measure their similarity.

Recommendation Generation: Based on user input (e.g., selected movie title or user preferences), the system identifies similar movies using cosine similarity scores and recommends them to the user.

* * *
# About project:

After downloading the dataset and running Pre_processing.py, you will obtain two key files: similairty_matrix.py and modified_dataset.csv. The smiliarity_matrix.npy file contains the computed similarity matrix for the movies, which is used for generating recommendations. The modified_dataset.csv file includes the preprocessed dataset, which has been cleaned and prepared for analysis and recommendation purposes.

Streamlit: Streamlit is an open-source Python library for creating interactive web apps for data science and machine learning projects
Next Website.py is compiled using the command 'streamlit run Website.py' because this is website built using Streamlit
On the webpage, users can input their preferred movies and receive the top 5 movie recommendations based on that selection

* *  *
# DEMO:
