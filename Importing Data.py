
#from ipython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import display

sns.set(style='darkgrid', context='talk', palette='Dark2')


if __name__ == '__main__':
    import praw

    reddit = praw.Reddit(client_id='yRWMyKR8lTnbHRxk1w1WDA',
                         client_secret='RDJHMQEhwRioRNKg0ZR4B6lNJYd0tQ',
                         user_agent='PsychologicalRest307',
                         check_for_async=False)

    subreddit = reddit.subreddit('roevwade2022')
    news = [*subreddit.top(limit=None)]
    print(len(news))
















    #headlines = set()

    #for submission in reddit.subreddit('roe_v_wade').new(limit=None):
    #headlines.add(submission.title)
    #display.clear_output()
    #print(len(headlines))

