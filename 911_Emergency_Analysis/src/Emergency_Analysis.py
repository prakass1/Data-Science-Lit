# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import Map as mp
import os

path = "G://Jupyter Notebook//Data Science//Refactored_Py_DS_ML_Bootcamp-master//10-Data-Capstone-Projects//"

### Read the CSV
data = pd.read_csv(path+"911.csv",sep=",")

data.head(2)

#### Emergency Types ###########
def filterEmergenciesCategory(val):
        if ":" in val:
          return  val.split(":")[0].strip()
    
def filterEmergency(val):
        if ":" in val:
          return  val.split(":")[1].strip().replace("-","").strip()

############## Filtering ###########
data["E-Category"] = data.title.apply(filterEmergenciesCategory)
data["E-Type"] = data.title.apply(filterEmergency)


data.head(2)
data["E-Type"][10]
data["E-Category"][12]


########### Count frequencies of Categories ##################
sns.countplot(x="E-Category",data=data)
plt.show()
plt.savefig("1.png")
top5Emergency = data["E-Type"].value_counts().head(5)
################# Accidents which are top-5 ############
sns.barplot(x=top5Emergency.index,y=top5Emergency.values)
plt.savefig("2.png")


############### Lets plot a lat and long map plot / Geo Plot ##############
data.dropna(inplace=True)
mp.plotMap(data)


############### Working with Time Series Data ############################
type(data["timeStamp"][0])
#Converting to timestamp format for observation
data["timeStamp"] = pd.to_datetime(data["timeStamp"])

#Exploring the datetime

daysofweek = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

data["year"] = data["timeStamp"].apply(lambda x: x.year)
data["month"] = data["timeStamp"].apply(lambda x: x.month)
data["date"] = data["timeStamp"].apply(lambda x: x.date())
data["hour"] = data["timeStamp"].apply(lambda x: x.hour)
data["minute"] = data["timeStamp"].apply(lambda x: x.minute)
data["day_of_emergency"] = data["timeStamp"].apply(lambda x: daysofweek[x.dayofweek])


########## What are the distibutions of days based on the type of emergency #########
sns.countplot(x="day_of_emergency", data=data, hue="E-Category")

###### 3months are missed due to some reason ############
sns.countplot(x="month", data=data, hue="E-Category")

##### Perform Aggregation of data #####
#Emergency Call by month plot
groupedByMonth = data.groupby("month").count()

plt.figure(figsize=(10,6))
plt.title("Calls obtained for Emergency by months")
plt.xlabel("Month")
plt.ylabel("Call Frequency")
plt.plot(groupedByMonth.index, groupedByMonth.zip)
plt.savefig("callfreq.png")




######### Time series plots ############################
# 1: Date plot
data.groupby("date").count()["zip"].plot()
plt.savefig("CallsTs.png")

# 2: By Each Category
plt.title("EMS")
data[data["E-Category"] == "EMS"].groupby("date")["zip"].count().plot()
plt.savefig("EMSTS.png")

plt.title("Traffic")
data[data["E-Category"] == "Traffic"].groupby("date")["zip"].count().plot()
plt.savefig("TrafficTS.png")

plt.title("Fire")
data[data["E-Category"] == "Fire"].groupby("date")["zip"].count().plot()
plt.savefig("FireTS.png")



######### HeatMap on the week ###############
trafficVals = data.groupby(by=["day_of_emergency","hour"]).count()["E-Category"].unstack()
plt.figure(figsize=(12,6))
sns.heatmap(trafficVals,cmap='viridis')
plt.savefig("heatmapEmergencies.png")

dayMonth = data.groupby(by=['day_of_emergency','month']).count()['E-Category'].unstack()
plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='rainbow')
plt.savefig("heatmapEmergenciesMonth.png")