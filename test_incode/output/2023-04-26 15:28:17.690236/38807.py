#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or adds a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == '':
            break
        else:
            print(number)
            
