#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or stores a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'exit':
            break
        else:
            print(number)
            