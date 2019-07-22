# --- Define your functions below! ---
def greetingfunction():
    print("hi there! I am the ultimate chatbot!!!!")
def additionfunction(num1, num2):

    print("I will add 2 numbers")
    answer = num1 + num2
    print(f"the answer is {answer}")
def respondToUser(userAnswer):
    if (userAnswer == 'good'):
        print("gald to hear! I'm good too")
    if (userAnswer == 'bad'):
        print(I'm sorry, How can I help)

# --- Put your main program below! ---
def main():
  while True: #while true is always true so it is always talking, it never "takes a break"
    # answer = input("(What will you say?) ")
    # print("That's cool!")
    print("hi")
    greetingFunction()
    # num1 = input("enter number 1")
    # num2 = input("enter number 2")
    # additionFunction()
    user_input = input("how are you?")
    respondToUser(user_input)







# # DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
