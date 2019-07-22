
# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.


tweetFile = open("tweets_small.json", "r")

tweetData = json.load(tweetFile)
print(len(tweetData))
# print(list(tweetData[0].keys()))
#keys of the first "dictionary"/tweet
# favorite_count = 0
#
# for i in range(0,len(tweetData)):
# 	if "favorite_count" in tweetData[i]:
#
# 		favorite_count += tweetData[i]['favorite_count']
#
# avg = favorite_count / len(tweetData)
# print(avg)
tweetlist = []
for i in range(0, len(tweetData)):
	if "text" in tweetData[i]:
		tweetlist.append(tweetData[i]["text"])
	else:
		continue

# print(tweetlist)

tweetFile.close()

for  j in range(0, len(tweetlist)):
	print(tweetlist[j])

# import counter
# print(tweetData[0].count('a'))
#
#
# favoriteCount, numberOfFavoriteCounts - 0,0
#
# def numOfLetter(tw, letter):
# 	count = 0
# 	for l in tw:
# 		if l == letter or l.lower() == letter:
# 			print(1)
# 			count += 1
# 	return count
#
# numA = 0
# #numB = 0
# for tweet in tweetData:
# 	if "text" in tweet:
# 		numA +- numOfLetter(tweet["text"], "a")
# 		#numB +- numOfLetter(tweet["text"], "b")
# print(numbA)
# #
# print(type(tweetData))
# print(tweetData[0])

#ATTEMPT 1 in word count
# for word in tweetData[0]:
# 	tweetFile = tweetFile.replace(word,'')
# tweetFile = tweetFile.lower()
# print(text)

#ATTEMPT 2
#initializing dict
# d = {}
# #count number of times each word comes up in list of words
# for word in tweetData:
# 	if word not in d:
# 		d[word] = 0
# 	d[word] += 1
# print(word)

# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])

# Encourage students to think about how there are
# often multiple solutions for each problem, and
# how each solution might have strenghts and drawbacks.
