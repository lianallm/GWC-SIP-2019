import json
f = open("answerD.json", "r")
s = json.load(f)
f.close()

sum_ages = 0

for i in s:
    age =int(i["How old are you?"])
    sum_ages += age
avg = sum_ages / len(s)
print(avg)
#comment
