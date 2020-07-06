#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:24:29 2020

@author: jamaalsmith
"""

import tweepy 
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "SZQPcpQeruvMDoQuowCOk4fwd" 
consumer_secret = "603EU5V98i7XI1bY6EKHfjiid0N88opdbR4eJYWQvdEM5AJNuE"
access_key = "22245392-WGVcnhQ8OiYoAbfT2uFaW2XY0eo8uyG0Jj71DUGdy"
access_secret = "rgdQTW32JQ39JMzCvDJsbMXHek0ilo3myol5ZlddXI7bw"
  
# Function to extract tweets 
def get_tweets_user(username,number_of_tweets): 
    """ This function pulls a designated number of tweets from a user"""
          
        # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
    auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
    api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
    number_of_tweets=number_of_tweets
    tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
    tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
    tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
    for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
        tmp.append(j)  
  
        # Printing the tweets 
        print(tmp) 


# Function to extract tweets based on query 
def get_tweets_query(query,rpp): 
    """ This function pulls a designated number of tweets from a query"""
          
        # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
    auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
    api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
    number_of_tweets=number_of_tweets
    tweets = api.search(q=query,lang='en',rpp=rpp)
  
        # Empty Array 
    tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
    tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
    for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
        tmp.append(j)  
  
        # Printing the tweets 
        print(tmp) 