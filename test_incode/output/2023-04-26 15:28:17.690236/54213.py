#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or returns numbers. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            apple = input("Enter a number: ")
            apple = apple * 2
            print(apple)
        elif fruit == "orange":
            orange = input("Enter a number: ")
            orange = orange * 2
            print(orange)
        elif fruit == "banana":
            banana = input("Enter a number: ")
            banana = banana 