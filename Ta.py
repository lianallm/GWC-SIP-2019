# --- Define your functions below! ---
import random

def greetings():
    print("---------------------------")
    print("Top of the morning to Yuh")

def name(answer):
    userAnswer2 = input(f"Would you like to play a game, {answer}.Yes or no?")
    print(userAnswer2)
    return userAnswer2


def game1(response):
    if( response == 'yes' or response== "Yes" ):
        possible = [" rock", "paper", "scissors"]
        h = random.choice(possible)
        userchoice = input(" Choose: rock, paper, or scissors")
        if h == userchoice:
            print("It's a tie")

        elif (h == "rock" and userchoice == "paper") or (h == "paper" and userchoice == "scissors") or  (h == "scissors" and userchoice == "rock"):
            print("You win!!!!")
        else:
            print(" You lose :()")

    elif( response == "no" or response =="No"):
        print('Your loss meanie,try again')


        # --- Put your main program below! ---

def main():
    while True:
        greetings()
        # answer = input("(What will you say?) ")
        # print("That's cool!")
        a = input("What is your name ?")

        #calls the function and returns the answer
        #set response to equal our aswer which is returned from name(a)
        response1 = name(a)
        if response1 == "yes":
            b = input ("Do you wanna play rock, paper, scissors!!!?")

            response2 = game1(b)





# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
