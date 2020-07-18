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
