#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers. """    
    numbers = range(1,10)
    
    while True:
        number = input("Enter a number: ")
        if number == "stop":
            break
        else:
            print(number)
            
