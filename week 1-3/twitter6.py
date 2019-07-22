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
# for g in range(len(tweetData)):
# 	dict = {}
# 	dict["ID"] = tweetData[g]['id']
# 	dict["polarity"] = pList[g]
# 	dict["tweets"] = tweetlist[g]
# 	userlist.append(dict)

#for  j in range(0, len(userlist)):
	# print(userlist[j])


tweetstring = ""
for d in tweetlist:
	estring = " "
	tweetstring += d

print(pList)
'''
#generates wordcloud
wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetstring)
plt.figure(figsize = (10,10), facecolor = None)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()
plt.savefig('lianaschart.png')
n, bins, patches = plt.hist(pList, 50, normed=1, facecolor='g', alpha=0.75)
'''
#histogram stuff
wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetstring)
print(min(pList), max(pList))
plt.hist(pList)
plt.axis([-0.55, 1.05, 0, 50])
plt.savefig('lianaschart2.png')

plt.show()




'''
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of Sentiment')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
'''
