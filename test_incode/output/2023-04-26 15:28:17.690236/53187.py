#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or opens user input. """    
    while True:
        number = input("Enter a number: ")
        if number == "quit":
            break
        else:
            print(number * 2)
