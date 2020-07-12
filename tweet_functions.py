#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:24:29 2020

@author: jamaalsmith
"""

def clean_COVID_df(df):
    """Quick function to remove unneeded columns from the tweet dataframes"""
    df = df.drop(columns=['id','conversation_id','created_at','user_id','reply_to'
                          ,'retweet_date','translate','trans_src','trans_dest'],inplace=True)
    return df