# from ipython import display
import math
from pprint import pprint

import datetime as dt
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, RegexpTokenizer  # tokenize words
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from itertools import chain
import seaborn as sns
import praw
from IPython import display
from wordcloud import WordCloud


def get_thread_from_reddit():
    reddit = praw.Reddit(client_id='yRWMyKR8lTnbHRxk1w1WDA',
                         client_secret='RDJHMQEhwRioRNKg0ZR4B6lNJYd0tQ',
                         user_agent='PsychologicalRest307',
                         check_for_async=False)
    subreddit = reddit.subreddit('Abortiondebate')
    news = [*subreddit.top(limit=None)]
    print(len(news))

    return news


def get_df_with_stats(news):
    news0 = news[0]
    print(news0.title)  # headline
    print(news0.score)  # upvotes
    print(news0.created)  # UNIX timestamps
    print(dt.datetime.fromtimestamp(news0.created))  # date and time
    print(news0.num_comments)  # no. of comments
    print(news0.upvote_ratio)  # upvote / total votes
    print(news0.total_awards_received)  # no. of awards given
    title = [news.title for news in news]
    news_df = pd.DataFrame({
        "title": title
    })
    print(news_df.head())

    return title, news_df


if __name__ == '__main__':
    news = get_thread_from_reddit()

    title, news_df = get_df_with_stats(news)

    # add sentiment analysis
    sid = SentimentIntensityAnalyzer()
    res = [*news_df['title'].apply(sid.polarity_scores)]
    pprint(res[:3])

    sentiment_df = pd.DataFrame.from_records(res)

    news_df = pd.concat([news_df, sentiment_df], axis=1, join='inner')
    print(news_df.head())

    THRESHOLD = 0.2

    conditions = [
        (news_df['compound'] <= -THRESHOLD),
        (news_df['compound'] > -THRESHOLD) & (news_df['compound'] < THRESHOLD),
        (news_df['compound'] >= THRESHOLD),
    ]

    values = ["neg", "neu", "pos"]
    news_df['label'] = np.select(conditions, values)

    #print(news_df.head())

    # print(news_df.label.value_counts())
    news_df.to_pickle('data\\news_df.pkl')



    # headlines = set()

    # for submission in reddit.subreddit('roe_v_wade').new(limit=None):
    # headlines.add(submission.title)
    # display.clear_output()
    # print(len(headlines))
