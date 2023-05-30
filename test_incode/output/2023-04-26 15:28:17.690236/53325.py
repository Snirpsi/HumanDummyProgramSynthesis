#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers. """    
    
    numbers = []
    
    while True:
        numbers.append(int(input("Enter a number: ")))
    
    print("Numbers entered: ", numbers)
    
