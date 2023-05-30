#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and calculates user input. """    
    while True:
        fruits = input("Enter a fruit (type 'quit' to quit): ")
        if fruits == 'quit':
            break
        else:
            fruits = fruits.lower()
            fruits = fruits.split()
            fruits = list(fruits)
            fruits.sort()
            print(