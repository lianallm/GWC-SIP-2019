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

# print(tweetlist)

#countletter (tweetstring, a)

def countletter(stringoftweet, string1):
	counter = 0
	string1 = string1.lower()
	wordList = stringoftweet.split(' ')
	for item in wordList:
		if item == string1:
			counter += 1
	return counter


alpha = ['a', 'c', 'k', 'x', 's', 'h', 'q', 'v', 'l', 'b', 'n', 'f', 'd', 'o', 'p', 'w', 'z', 'm', 'y', 'i', 'e', 'g', 'r', 'j', 'u', 't']

letters = sorted(alpha)
# print(len(alpha))

x_axis = letters
y_axis = []
for item in tweetlist:
	# print(f"letter: {letter} occurences:{countletter(tweetstring, letter)}")
	wordoccurance = countletter(item, "the")
	# yvalue = countletter(tweetstring, letter)
	y_axis.append(wordoccurance)

# print(y_axis)


#histogram of t h # -*- coding: utf-8 -*-

n, bins, patches = plt.hist(y_axis, 50)
plt.axis([min(y_axis), max(y_axis), 0,50])
plt.grid(True)
plt.show()


# countletter(tweetstring, set(sorted(alpha)))

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



'''
#histogram stuff
wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetstring)
# print(min(pList), max(pList))
plt.hist(pList)
plt.axis([-0.55, 1.05, 0, 50])
plt.savefig('lianaschart2.png')

# plt.show()
'''



'''
#histogram of num of letters
wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetstring)
# print(min(y_axis), max(y_axis))
plt.hist(y_axis)
plt.axis([min(y_axis), max(y_axis), 0,10])
# plt.savefig('lianaschart2.png')
plt.show()
'''

'''
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of Sentiment')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
'''
