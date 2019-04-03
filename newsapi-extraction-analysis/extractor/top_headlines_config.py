############################
#author: Subash Prakash
#Description: Configuration for extraction of newsapi into csv for analysis
############################

# Url
url = 'https://newsapi.org/v2/top-headlines?' + \
      'country=us' + \
      '&apiKey='

####### Category
category = ["business", "general", "science", "sports", "technology", "gaming", "health"]

##### Page Size 50
pageSize = 50

### CSV Directory and File
csv_file = "E://input//"
headers = ['name','author','title','description','url','publishedAt','category']