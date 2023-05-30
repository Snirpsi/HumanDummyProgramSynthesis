#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or multiplyes words. """    
    while True:
        fruit = input("Enter a fruit: ")
        fruit = fruit.lower()
        if fruit == "apple":
            print("You chose apple!")
        elif fruit == "banana":
            print("You chose banana!")
        elif fruit == "cherry":
            print("You chose cherry!")
        elif fruit == "