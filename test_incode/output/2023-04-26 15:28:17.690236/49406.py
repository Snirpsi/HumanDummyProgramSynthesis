#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits and multiplyes user input. """    
    while True:
        fruit = input("Enter a fruit: ")
        fruit = fruit.lower()
        if fruit == "apple":
            print("The fruit is", fruit, "and multiplied by 