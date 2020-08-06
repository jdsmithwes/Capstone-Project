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
