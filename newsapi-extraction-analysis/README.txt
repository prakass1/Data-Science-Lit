# Explanation of setup and extraction script:

Extract the zip into in any location of your choice.

1. Setup:
To run any of this first, you will need python being installed and then anaconda/ full setup of all libraries.

-- Installation of python:
Windows:
Steps:
1. Go to https://www.python.org/downloads/ and download the setup for python and install it. Once, that is setup ensure that the environment variable are all set for python by checking below command on windows command prompt:
-- Open command prompt
-- type python --version ## This should return a version, if not the environment variables are not setup correctly.
-- Setup pip next using this tutorial: https://pip.pypa.io/en/stable/installing/
-- Now you are all ready with install all required libraries for running python machine learning code.

2. This repo also contains a requirements.txt using which one can install all the libraries on the fly at once.
-- cd into the extracted folder and run pip install -r requirements.txt. With all things in place this should setup all required libraries correctly

Now, one is ready to launch jupyter-notebook or run the extraction.

Alternative (Easy):
-- Installation of Anaconda:
Anaconda is a virtual environment which already comes with latest libraries for machine learning and usages.
Install Anaconda using this link : https://www.anaconda.com/
Setup everything properly and after installation using anaconda navigator install the required libraries:
1. pandas
2. seaborn==0.9.0
3. matplotlib
4. sklearn
5. numpy
6. yellowbricks
7. gensim
8. pyldavis
9. wordcloud
10. nltk

If any libraries are missed anyway there would be error and would need to be installed


3. Running the Extraction Script:
The extraction script is divided into parts:
1. top_headlines_config.py
This is a configuration file which needs to be done before even running the extractor:
Configs:

1.
url = 'https://newsapi.org/v2/top-headlines?' + \
      'country=us' + \
      '&apiKey=<<your-api-key>>'

-- Url contains the actual url and country and apiKey as a query parameter to the get request. This returns the json response of the topheadlines
	  
2.
category = ["business", "general", "science", "sports", "technology", "gaming", "health"]

-- All the categories of the news. This is randomly pick at each request from the extractor

3.
pageSize = 50

-- Ideally, request can also have a pageSize. But, this does not apply to topheadlines. Hence, is a optional parameter

4.
### CSV Directory and File
csv_file = "E://input//"
headers = ['name','author','title','description','url','publishedAt','category']

-- csv_file - This indicate to which location should the csv be saved. This should be configured accordingly.
-- headers -- All the required fields in the csv for data extraction. This is configurable meaning if other data needs to be extracted it can also be done more genrically.

2. top_headlines_extractor.py
This is an extractor script to extract the top headlines from newsapi. All descriptions are directly provided in the script itself.



References:
1. https://newsapi.org/docs 
2. https://scikit-learn.org/0.18/auto_examples/text/document_clustering.html
3. https://radimrehurek.com/gensim/models/ldamodel.html
4. https://www.wellbeingatschool.org.nz/information-sheet/understanding-and-interpreting-box-plots
5. https://amueller.github.io/word_cloud/
6. https://seaborn.pydata.org/
7. https://github.com/bmabey/pyLDAvis/tree/master/notebooks