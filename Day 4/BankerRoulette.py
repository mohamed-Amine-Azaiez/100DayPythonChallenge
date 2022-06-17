import random

names=input("Give me everybody's names, seperated with a comma.\n").split(", ")
nb=len(names)

randomnb= random.randint(0,nb-1)
print(names[randomnb] + " is going to pay the meal today !")
