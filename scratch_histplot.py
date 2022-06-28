
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    news_df = pd.read_pickle('data\\news_df.pkl')

    print(news_df.head(5))

    sns.histplot(news_df.label)
    plt.show()