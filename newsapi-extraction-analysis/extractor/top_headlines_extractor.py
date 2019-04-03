# author: Subash Prakash
# Description: A extraction file to extract the responses from the news api
# and convert it into a csv

## Import libraries
import requests as req
import json
import time
import sys
import numpy as np
import os
import csv
import random
import top_headlines_config as config

## Categories and pagesize as query params
q_pageSize="&pageSize="
q_category="&category="
##############################

# Adding a separator. Here "|" is chosen because ",/:/;" could be in text
sep = "|"


##################################
#name: makeRequest(category)
#parameters: category
#Description: This method will make a
# request based on the category provided.
##################################
def makeRequest(category):
    url = config.url + q_category + str(category)
    response = req.request("get", url)
    if response.status_code == 200:
        return response.json()
    else:
        print("There has been error in the request " + str(response.status_code))

##################################
#name: prepareData(headlines,category)
#parameters: headlines (response), category
#Description: This method will open a csv and write to it by parsing the json response
##################################
def prepareData(headlines,category):
        try:
            with open(config.csv_file + "headlines.csv", "a", newline="", encoding="utf-8") as f:
                contentwriter = csv.writer(f, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for article in headlines["articles"]:
                    line = [str(article["source"]["name"]), str(article["author"]),
                            str(article["title"]), str(article["description"]),
                            str(article["url"]), str(article["publishedAt"]),
                            #str(article["content"]),
                            category
                            ]
                    contentwriter.writerow(line)
            f.close()
            return 0
        except IOError:
            print("Looks like there is an IO error !!!!")
            return 1

###### Start of Main ###########

#### Ideal ###################
#hours = 1
#minutes = 60
#min_to_req = 10
#request_range = int((hours * minutes) / min_to_req)

# Here the range of request is set. Meaning how many times the request is be fired.
# Note: If the sleep time is low, then there could be many duplicate responses.
request_range = 20
for _ in range(request_range):
    rand_category = (random.choice(config.category))
    headlines_json = json.dumps(makeRequest(rand_category))
    headlines = json.loads(headlines_json)
    #Make the csv for text analysis
    fileExists = os.path.isfile(config.csv_file + 'headlines.csv')
    if not fileExists:
        print("Writing the file for the first time")
        f = open(config.csv_file + "headlines.csv", "w",newline="", encoding="utf-8")
        writer = csv.writer(f, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(config.headers)
        f.close()
    returnCode = prepareData(headlines, rand_category)
    if returnCode == 1:
        print("Looks like there is a issue with file operations check it and rerun the script")
        sys.exit(1)
    # Sleep for the equal amount of division time in ideal case.
    # Now the value is set for 60 seconds. It can be changed.
    time.sleep(60)
    print("Started writing again")

# If all the data is correctly provided, the data will be extracted as a csv in the provided location
print("The data is now collected, extracted and written !!!")