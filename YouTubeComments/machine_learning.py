# TFIDF Vectorize
# BagOfWords Vectorize
# Any visual?
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import os



def my_tokens(text):
    return ["".join(word) for word in text.split()]


import numpy as np

def buildClassifier(df, bigram=False):
    if bigram:
        tfidf = TfidfVectorizer(tokenizer=my_tokens, ngram_range=(2, 2))
    else:
        tfidf = TfidfVectorizer(tokenizer=my_tokens)
    #bow = CountVectorizer(tokenizer=my_tokens)
    #bow_vectors = bow.fit_transform(df["CONTENT"])
    vectors = tfidf.fit_transform(df["CONTENT"])
    dense_v = vectors.todense()
    #dense_bv = bow_vectors.todense()

    # dense_v.shape
    #denser_b = np.append(dense_bv, df[["hashtag_count"]], axis=1)
    #denser_b = np.append(dense_bv, df[["link_count"]], axis=1)

    denser_1 = np.append(dense_v, df[["hashtag_count"]], axis=1)
    denser_2 = np.append(denser_1, df[["link_count"]], axis=1)
    #denser_3 = np.append(denser_2, df[["comm_word_len"]], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        denser_2, df["CLASS"], test_size=0.3, random_state=42)
    svm = SVC(gamma="auto", C=1.0, kernel="linear")
    #param_grid = {
    #    "C": [0.1, 0.3, 0.5, 0.7, 0.9, 1.0, 10, 100],
    #    "kernel": ["rbf", "linear", "poly"]
    #}

    #grid_cv = GridSearchCV(svm, param_grid=param_grid, verbose=True, cv=10)
    svm.fit(X_train, y_train)
    #grid_cv.fit(X_train, y_train)
    #grid_cv.best_params_
    #grid_cv.best_score_
    #grid_cv.cv_results_
    '''
    {'C': 1.0, 'kernel': 'linear'}

    '''
    svm_predict = svm.predict(X_test)
    #g_predict = grid_cv.predict(X_test)
    print("SVM results ------------------------- \n")
    print(classification_report(svm_predict, y_test))
    print("--------------------------------------------------\n")
    mnb = MultinomialNB()
    bnb = BernoulliNB()
    mnb.fit(X_train, y_train)
    bnb.fit(X_train, y_train)
    mpredict = mnb.predict(X_test)
    bpredict = bnb.predict(X_test)
    print("MultiNomial NB results ------------------------- \n")
    print(classification_report(mpredict, y_test))
    print("--------------------------------------------------\n")
    print("Bernoulli NB results ------------------------- \n")
    print(classification_report(bpredict, y_test))
    print("--------------------------------------------------\n")
    return svm_predict, mpredict, bpredict, y_test

import itertools
def write_to_file(label, svm_predictions, mpredictions, bpredictions):
    out_file = open("output.csv", "w", encoding="utf-8")
    out_file.write("Actual-Class, Text, SVM-Prediction, MultinomialNB-Predictions, Bernoulli-Predictions, \n" )
    for actual, sp, mp, bp in itertools.zip_longest(label, svm_predictions, mpredictions, bpredictions):
        out_file.write(str(actual) + ", " + str(sp) + ", " + str(mp) + ", " + str(bp) + ",\n")
    out_file.close()

