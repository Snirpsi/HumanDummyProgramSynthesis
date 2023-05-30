#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or removes user input. """    
    while True:
        number = input("Enter a number: ")
        if number == '':
            break
        else:
            print(number)
            
