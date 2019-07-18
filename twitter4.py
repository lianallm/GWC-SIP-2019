import json
from textblob import TextBlob
import matplotlib.pyplot as plt

from wordcloud import WordCloud


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


userlist = []
	#tweetsDatat[i][id]
for g in range(len(tweetData)):
	dict = {}
	dict["ID"] = tweetData[g]['id']
	dict["polarity"] = pList[g]
	dict["tweets"] = tweetlist[g]
	userlist.append(dict)

#for  j in range(0, len(userlist)):
	# print(userlist[j])


wordcloud = WordCloud().generate("text")

tweetstring = ""
for d in tweetlist:
	estring = " "
	tweetstring += d
print(tweetstring)

#Display the generated image:

plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()
plt.savefig('lianaschart.png')
