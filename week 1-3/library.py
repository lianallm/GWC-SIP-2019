# friends = {
#   'Mariela' : 17,
#   'Liana' : 17,
#   'Dana' : 17,
#   'Ally' : 21,
#   'Connie' : 19,
#   'Nicole' : 17,
#   'Izear' : 15,
#   'Ngina' : 16,
#   }
# print(friends)

import json

def takesurvey(questions, answers):
    # print(answers)
    answerD = {}
    for q in questions:
        answerD[q] = input(q) # whatever input(q) is is the user
        # print(answerD)
                                # answer therefore its the value
    # print(answerD)
    answers.append(answerD)

a = []

q = ["What is your name?", "How old are you?", "What is your favorite color?", "What color is your hair?"]

for i in range(5):
    if input("Continue yes/no") == "yes":
        print("new survey")
        # a.append({"Lianna":17,"Mariela":17}) #just for debugging
        takesurvey(q, a)
    else:
        break


# print(a) # a is the list of dictionaries
# a.append({"Lianna":17,"Mariela":17})

f = open("answerD.json", "w")
f.write(json.dumps(a)) #dictionary and lists (python code) into valid json text
#json.dump(a,f) try that, f is defined in line 36, file object
f.close()
#---------------


# users = {}
#
# username = input("What is your name?")
#
# questionlist = ["How old are you?", "What's your favorite color?", "What's your favorite subject?"]
# for q in questionlist:
#     answer = []
#     answer[q] = input(q)



#make username a  key inside dictionary
#ask questions
#have answers append into a list corresponding to their key
