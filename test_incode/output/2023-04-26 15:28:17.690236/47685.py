#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns fruits or returns user input. """    
    fruit = input("What fruit do you want? ")
    fruit = fruit.lower()
    fruit = fruit.strip()
    
    if fruit == "apple":
        print("Apple")
    elif fruit == "banana":
        print("Banana")
    elif fruit == "cherry":
        print("Cherry")
    elif fruit == "date":
        print("Date")
    elif fruit == "dog":
        print("Dog")
    elif fruit == "duck":
        print("Duck")
    elif fruit == "elephant":
        print("Elephant")
    elif fruit == "fruit":
        print("Fruit")
    elif fruit == "grape":
        print("Grape")
    elif fruit == "grapefruit":
        print("Grapefruit")
    elif fruit == "orange":
        print("Orange")
    elif fruit == "pear":
        print("Pear")
    elif fruit == "pineapple":
        print("Pineapple")
    elif fruit == "pizza":
        print("Pizza")
    elif fruit == "pumpkin":
        print("Pumpkin")
    elif fruit == "red":
        print("Red")
    elif fruit == "salmon":
        print("Salmon")
    elif fruit == "strawberry":
        print("Strawberry")
    elif fruit == "tangerine":
        print("Tangerine")
    elif fruit == "watermelon":
        print("Watermelon")
    elif fruit == "yellow":
        print("Yellow")
    else:
        print("Sorry, I didn't understand that.")
