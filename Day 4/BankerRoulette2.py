import random


names=input("Give me everybody's names, seperated with a comma.\n").split(", ")
print(random.choice(names) + " is going to pay the meal today !")
