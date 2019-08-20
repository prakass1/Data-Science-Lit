import matplotlib.pyplot as plt
import seaborn as sns
import re
from scipy.stats import norm
import numpy as np

sns.set_palette("viridis")
sns.set_style("whitegrid")

####### Custom importing

try:
    import preprocessing as pp
except ImportError:
    print("Looks like the file does not exist")

#Understanding and implementing a pattern search algorithm
#For now use re

def draw_dist(full_df):

    fig, ax = plt.subplots(ncols=2,figsize=(10,6))
    sns.distplot(full_df[full_df.CLASS == 0]["comm_word_len"], kde=False, bins=20, hist=True, ax=ax[0], axlabel="Ham Comments")
    ax[0].set_title("Ham comments word distribution")
    sns.distplot(full_df[full_df.CLASS == 1]["comm_word_len"], kde=False, bins=20, hist=True, ax=ax[1], axlabel="Spam Comments")
    ax[1].set_title("Spam comments word distribution")
    plt.tight_layout()
    plt.show()
    plt.savefig("word_length.png")

def draw_count_plot(full_df):
    plt.title("Distribution of Class")
    sns.countplot(x="CLASS", data=full_df)
    plt.savefig("countplot_class.png")
    fig,ax = plt.subplots(ncols=2,figsize=(10,8))
    plt.tight_layout()
    sns.countplot(x="CLASS",data=full_df,hue="hashtag_count",ax=ax[0])
    ax[0].set_title("Hash Tags over Spam and Ham comments")
    sns.countplot(x="CLASS", data=full_df, hue="link_count",ax=ax[1])
    ax[1].set_title("Links over Spam and Ham comments")
    plt.savefig("comb_plt_class.png")

def draw_corr(full_df,size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot
    '''

    corr = full_df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.grid(False)
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.savefig("corr_data.png")