import plotly.io as pio
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.dummy import DummyRegressor
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from yellowbrick.regressor import PredictionError
from yellowbrick.classifier import ConfusionMatrix
from yellowbrick.classifier import classification_report
from yellowbrick.classifier import ROCAUC
import xgboost as xgb

def plotly_line (df,x,y):
    """Function that provides line graphs in Plotly Express"""
    fig = px.line(df,x=x, y=y)
    fig.show()

def plotly_scatter(df,x,y,trendline,color):
    """Function for creating a scatterplot in Plotly Express"""
    fig = px.scatter(df,x, y=y,color=color,trendline=trendline)
    fig.show()

def Plotly_bar(df,x,y,title,color):
    """Function for creating a plotly express bar chart"""
    fig = px.bar(df, x=x, y=y, title=title,color=color)
    fig.show()


def ROC_Curve (Model, X,y):
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.15)
    model = Model
    visualizer = ROCAUC(Model)

    visualizer.fit(X_train, y_train)        # Fit the training data to the visualizer
    visualizer.score(X_test, y_test)        # Evaluate the model on the test data
    visualizer.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:24:29 2020

@author: jamaalsmith
"""
import pandas as pd
import numpy as np


def clean_COVID_df(df):
    """Quick function to remove unneeded columns from the tweet dataframes"""
    df = df.drop(columns=['id','conversation_id','created_at','user_id','reply_to'
                          ,'retweet_date','translate','trans_src','trans_dest'],inplace=True)
    return df

def write_exel(df, output_name):
    """Quick function to write excel files from dataframes
    df = name of dataframe you want to write_exel
    output_name = name of file you want to write"""
    # create excel writer object
    writer = pd.ExcelWriter('covid_data.xlsx')
    # write dataframe to excel
    covid_data.to_excel(writer)
    # save the excel
    writer.save()
    print('DataFrame is written successfully to Excel File.')

#from gensim.parsing.preprocessing import remove_stopwords
#from pd import DataFrame
def create_document_term_matrix(message_list, vectorizer):
    #from pandas import DataFrame
    doc_term_matrix = vectorizer.fit_transform(message_list)
    df = pd.DataFrame(doc_term_matrix.toarray(), columns= vectorizer.get_feature_names())

    return df

def tsne_plot(model):
    "Creates and TSNE model and plots it. This function was originally found on Kaggle"
    labels = []
    tokens = []

    for word in model.vocab:
        tokens.append(model[word])
        labels.append(word)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(16, 16))
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()

from sklearn.manifold import TSNE
def display_closestwords_tsnescatterplot(model, word, size):

    arr = np.empty((0,size), dtype='f')
    word_labels = [word]
    close_words = model.similar_by_word(word)
    arr = np.append(arr, np.array([model[word]]), axis=0)
    for wrd_score in close_words:
        wrd_vector = model[wrd_score[0]]
        word_labels.append(wrd_score[0])
        arr = np.append(arr, np.array([wrd_vector]), axis=0)

    tsne = TSNE(n_components=3, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)
    x_coords = Y[:, 0]
    y_coords = Y[:, 1]
    plt.scatter(x_coords, y_coords)
    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
        plt.xlim(x_coords.min()+0.00005, x_coords.max()+0.00005)
        plt.ylim(y_coords.min()+0.00005, y_coords.max()+0.00005)
    plt.show()

def EDA_Summary(data,title,output_file):
    """Function to get panda profile for EDA purposes
    data: Enter either the dataframe or the file that can be read into pandas
    title: use string for title you want to use
    output_file: use string for the file that will host output"""

    data =  data
    profile = data.profile_report(title= title)
    profile.to_file(output_file= output_file)
    profile.to_notebook_iframe()

def pickle_save(object,file):
    """Function to save objects via pickling. The object is
    the item you want to save. The file is the name of the file/path where
    you want it stored"""

    pickle.dump( object, open( "file.p", "wb" ) )

def pickle_load(file):
    """ Function to load pickled items."""

    pickle.load( open( "file.p", "rb" ) )
