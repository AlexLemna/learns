import random

listoffruit = [
    "apple",
    "banana",
    "pear",
    "peach",
    "mango",
    "strawberry",
    "blueberry",
    "snozzberry",
]

def randomfruit():
    fruit = random.choice (listoffruit)
    print (f"Here, have a {fruit}.")

def repeatfunction(x, y):
    for integer in range (0,y):
        x()

print ("How many pieces of fruit do you want?")
userInput = int (input ("Enter a number: "))
repeatfunction(randomfruit, userInput)

