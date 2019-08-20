'''
This is section for preprocessing the raw csv data of comments of
Youtube for specific artists
'''

import pandas as pd
import numpy as np
import re
import os
import datetime
import nltk
import smiley_constructor
file_prefix = "Youtube_"

# Helpful someday

# emoji_pattern = re.compile("["
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#         u"\U0001F1F2-\U0001F1F4"  # Macau flag
#         u"\U0001F1E6-\U0001F1FF"  # flags
#         u"\U0001F600-\U0001F64F"
#         u"\U00002702-\U000027B0"
#         u"\U000024C2-\U0001F251"
#         u"\U0001f926-\U0001f937"
#         u"\U0001F1F2"
#         u"\U0001F1F4"
#         u"\U0001F620"
#         u"\u200d"
#         u"\u2640-\u2642"
#         "]+", flags=re.UNICODE)

#text = emoji_pattern.sub(r'', "This Dog")

def read_data(data_dir = "."):
    '''
    :param data: This defaults to current directory. If other directory it has
    to provided during the function declaration
    :return: It will return a combined data frame of all comments put in the data
    directory
    '''

    files = os.listdir(data_dir)

    #Concat Dataframe
    if not data_dir.endswith("//"):
        data_dir = data_dir + "//"
    combined_df = pd.concat([pd.read_csv(data_dir + f, encoding="UTF-8" ) for f in files], ignore_index=True)
    combined_df = combined_df.reset_index()
    return combined_df


def checklink_and_hashtag(x,linkFlag=False):
    if linkFlag == True:
        regx_pat = "(www\.|http:|https:)+[^\s]+[\w]"
    else:
        regx_pat = "(#[a-zA-Z])\w+"

    matches = re.findall(regx_pat, x)

    if len(matches) == 0:
        return 0
    else:
        return len(matches)

def stopwords_count(x):
    from nltk.corpus import stopwords
    stopwords = stopwords.words("english")
    return len([k for k in x.split() if k in stopwords])



def create_features(full_df):
    print("Adding column Comments Word Length")
    full_df["comm_word_len"] = full_df["CONTENT"].apply(lambda x: len(x.split(" ")))
    print("Adding column hashtag count")
    full_df["hashtag_count"] = full_df["CONTENT"].apply(lambda x: checklink_and_hashtag(str(x)))
    print("Adding column has link count")
    full_df["link_count"] = full_df["CONTENT"].apply(lambda x: checklink_and_hashtag(str(x), linkFlag=True))
    print("Adding column for stop words count")
    full_df["stop_words_count"] = full_df["CONTENT"].apply(lambda x: stopwords_count(str(x)))
    return full_df


def correct_spelling(word):
    '''
    This function implements an operation to correct any mis spelled words so that they could be as part of classification.
    Example: If the word is amazzziiing, then this function will correct it to amazing.

    :param word:
    :return: corrected word
    '''
    from spellchecker import SpellChecker
    check = SpellChecker()
    ### Make a pattern to get all letters which are greater than 2 times
    pattern = re.compile(r"(.)\1{2,}")
    ### Back reference the text to the same pattern to return 2 letter matches
    text_corr = pattern.sub(r"\1\1", word)
    #Correct that with spell checker (Read: Peter Norvig blog --> http://norvig.com/spell-correct.html)
    return check.correction(text_corr)


def preprocess(df, col_name="",lower=True,
               r_stopwords=True, r_special=True,
               r_rare=True,r_comm=True,
               lemma=True, spell_corr=True, emotion_corr = False):
    '''
    This function does the following things:
    1. Read each comment and lowercase
    2. Read each comment which is lower cased and remove stopwords
    3. Remove any special characters (@, :), etc)
    4. Spell Correction
    5. Lemmatization (Porter Stemmer)
    6. Rare words removal

    :description:
    It takes a list with options to perform.
    Use the below options (optional):
    1. To perform all the operations:
    simply call preprocess() - This defaults to all the operations

    2. To perform specific operations set all to False and use the operations in a list:
    lower: lowercase the sentence
    r_stopwords: remove stopwords
    r_special: remove special characters
    spell_corr: correction of spelling
    lemma: lemma using porter stemmer
    r_rare: rare words removal
    r_comm: Common words removal

    All are True by default, one can set specific to true as well

    Example:

    :return: a pre processed dataframe
    '''
    if lower:
        #lowercase
        df[col_name] = df[col_name].apply(lambda x: " ".join(x.lower() for x in x.split()))
    if r_stopwords:
        #stopwords
        from nltk.corpus import stopwords
        stopwords = stopwords.words("english")
        df[col_name] = df[col_name].apply(lambda x: " ".join(x for x in x.split() if x not in stopwords))
    if r_special:
        #special characters removal except (.)
        regex="[^\/\:\.\w\s]"
        df[col_name] = df[col_name].str.replace(regex, "")

    if spell_corr:
        df[col_name] = df[col_name].apply(lambda x: " ".join(correct_spelling(x) for x in x.split()))

    if r_comm:
        #Common Words removal which could mostly in all text and could be removed
        freq = pd.Series(' '.join(df[col_name]).split()).value_counts().head(10)
        df[col_name] = df[col_name].apply(lambda x: " ".join(x for x in x.split() if x not in freq))

    if r_rare:
        # Rare Words removal which could mostly in all text and could be removed
        rare = pd.Series(' '.join(df[col_name]).split()).value_counts().tail(10)
        df[col_name] = df[col_name].apply(lambda x: " ".join(x for x in x.split() if x not in rare))

    if emotion_corr:
        #Correct emotion to words
        sm = smiley_constructor.Smileys(smiley_constructor.emotions)
        df[col_name] = df[col_name].apply(sm.detect_word4smiley)

    #Remove empty
    df = df[df[col_name] != ""]
    return df


