
word = "empathy"
word = word.lower()
wordList = list(word)
finalword = ['e','m','p','a','t','h','y']

currentword = "_"*len(word)
currentword_list = list(currentword)

tries = 7

while (tries > 0):

	# use to test your code:
	# print(word)
	guess = input("Guess of a letter: ")
	guess = guess.lower()
	# converts the world to lowercase

	if(guess in wordList):
		index1 = wordList.index(guess)
		currentword_list[index1] = guess

	tries -= 1
	print(currentword_list)

if finalword == ['e','m','p','a','t','h','y']:
	print("congratulations")
