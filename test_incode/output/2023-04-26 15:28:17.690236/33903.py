#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and returns user input. """    
    while True:
        number = input("Enter a number: ")
        if number == "done":
            break
        else:
            print(number)
