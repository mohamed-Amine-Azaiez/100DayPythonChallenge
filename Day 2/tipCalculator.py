from unittest import result


print("Welcome to the tip calculator!")

bill= float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))/100
pp= int(input("How many people to split the bill? ")) 

result= (bill *(1+tip) )/pp
result= round(result,2)
print(f"Each person should pay: {result}")