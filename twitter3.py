
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

tweetFile = open("tweets_small.json", "r")

tweetData = json.load(tweetFile)

tweetlist = []
for i in range(0, len(tweetData)):
	if "text" in tweetData[i]:
		tweetlist.append(tweetData[i]["text"])
	else:
		continue

pList = []
for item in tweetlist:
	blob1 = TextBlob(item)
	polar1 = blob1.polarity
	pList.append(polar1)

# print(pList)
tweetFile.close()

# for  j in range(0, len(tweetlist)):
# 	print(tweetlist[j])
#^format only; puts each tweet to their own line

#make list of dictionaries with keys: "tweetID" "tweet" "polarity"

userlist = []
	#tweetsDatat[i][id]
for g in range(len(tweetData)):
	dict = {}
	dict["ID"] = tweetData[g]['id']
	dict["polarity"] = pList[g]
	dict["tweets"] = tweetlist[g]
	userlist.append(dict)

for  j in range(0, len(userlist)):
	print(userlist[j])
