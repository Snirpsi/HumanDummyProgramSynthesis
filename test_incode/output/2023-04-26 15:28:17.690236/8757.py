#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "quit":
            break
        else:
            print(number)
            
