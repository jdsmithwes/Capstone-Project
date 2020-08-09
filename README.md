# Capstone-Project
<h1><center>Predicting Public Response to Covid Based on Twitter Data</center></h1>


## Contents

I created specialized notebooks for various aspects of the analysis that are designed to work in unison. Below, please find the links for individual notebooks to ease your navigation through this project.

- [Twitter Data Collection](Twitter_dataqueries_capstone.ipynb)
- [Data Set Creation](Dataset_creation_notebook.ipynb)
- [Poll Data](Web Scraping Notebook.ipynb)
- [Explorator Data Analysis](EDA_notebook.ipynb)
- [Modeling](Models.ipynb)

## Objective

For the purpose of this analysis, I will attempt to measure the public's response to the Covid pandemic.  This study is important as the reopening of our society, from going to get an ice cream cone to being able to earn a living, hinges on our ability to lower the rate of infection in our country. For this rate to be lowered, individuals must feel that actions by public officials and governments are legitimate, effective and reasonable. Data obtained through the collection of tweets allows for real-time assessment of American's sentiment around both the Covid pandemic, and, more importantly during an election year, whether or not the government's response has risen to the challenge presented by this virus.

## [Data](Dataset_creation_notebook.ipynb)

To create the dataset, I utilized the [TWINT](Twitter_dataqueries_capstone.ipynb) library to collect tweets from January 1,2020 until August 8, 2020. I then made various subsets of the tweets. For example, to measure the impact of tweets by public leaders viewed as polar opposites regarding their response to the pandemic, I collected tweets by President Trump and the Governor of New York, Andrew Cuomo. Another subset of tweets that I labeled as baseline consists of tweets by the New York Times and Washington Post - two of America's leading journalism outlets.

The purpose of creating these subsets is that the baseline tweets can be considered to be those that communicate mainly fact. While they might have op-ed columnists, we can assume that most tweets from the news reporting divisions will provide factual updates on the Covid response. By considering the two polar opposites, Trump and Cuomo, we can measure Covid outcomes, in terms of cases, after the tweets have been consumed by the public. 

To collect data about the number of Covid cases and deaths, I utilized the data collected by the [Atlantic's Covid Tracking Project](https://covidtracking.com/). Data on the state level was collected from the [NYTimes respository](https://github.com/nytimes/covid-19-data). Finally, to get poll data, I consulted [RealClear Politics](https://www.realclearpolitics.com/epolls/2020/president/us/general_election_trump_vs_biden-6247.html).

## Goal of Analysis

Initially, it was the hope of this analysis to predict final election results in the 2020 Election based on the public's sentiment related to the Covid response. However, with most current polls showing presumptive democratic nominee Joseph Biden in the lead, preliminary models were attaining 99% accuracy scores. Even after controlling for features with oversized importance, models still scored extremely high without tuning. At this point, I augmented the goal to now classify the tweet as either being a good response or bad response. 

While initally feeling disappointed about this mid-project adjustment, inclusion of [Latent Diralecht Allocation](EDA_notebook.ipynb) allowed us to cluster the tweets into 10 topic areas. Thus, with the response type known, we can garner insights into what subset of the response the public shares that specific input. With this in mind, this analysis still offers some value to those following the 2020 Presidential election as political operatives can augment their campaign's message to place their candidate in the most favorable light with the electorate.
