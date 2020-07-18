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
from pd import DataFrame
def create_document_term_matrix(message_list, vectorizer):
    from pandas import DataFrame
    doc_term_matrix = vectorizer.fit_transform(message_list)
    df = pd.DataFrame(doc_term_matrix.toarray(), columns= vectorizer.get_feature_names())

    return df
