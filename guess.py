from random import * #this means: it gets you the ability to use randint lateron in the code (will discuss later)
#                   the asterisk means you "take" all the random functions available in that library, one of which is randint
#generates a random integer
aRandomNumber= randint(1,20)
# print(aRandomNumber) #for checking
tries = 3 #need to mae sure dont waste it on "hello" only when put in numbers (see orig ifnot else)
while tries > 0
guess = input("guess a random number between 1 and 20(inclusive):")
if not guess.isnumeric():#checks if a string is only digits 0-9
    print("that's not a positive whole number, try again")
else:
    tries -=1 #shorthand for tries = tries - 1
    guess = int(guess) #converts a string to an integer
    print(f"our guess is {guess}, our random number is {aRandomNumber} ) #f allows you to use brackets instead of +

    if(guess == aRandomNumber:)
        print("congrats")
        #to exiyt out of loop:
        break
    elif guess > aRandomNumber
        print("your guess is higher than my  number")
    else guess > aRandomNumber
        print("your guess is lower than my  number")

print(f"number of tries: {tries}")
print("you lose")
