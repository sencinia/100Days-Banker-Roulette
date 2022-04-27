import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


draw = random.randint(0, len(names))

print(names[draw] + " is going to buy the meal today!")
