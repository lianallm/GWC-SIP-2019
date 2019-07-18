# --- Define your functions below! ---
def greetingFunction():
    print("Hi there, I am chatbot!")
def respondToUser(userAnswer):
    if(userAnswer == "good"):
        print("I'm happy to hear, I'm good too")
    if(userAnswer == "bad"):
        print("awww... that's too bad")

# --- Put your main program below! ---
def main():
    greetingFunction()
    while True:
    # answer = input("(What will you say?) ")
    # print("That's cool!")

        user_input = input("how are you today?")
        respondToUser(user_input)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
