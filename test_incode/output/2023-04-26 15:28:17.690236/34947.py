#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or enumerates a list of words. """    
    while True:
        number = input("Enter a number: ")
        if number == 'exit':
            break
        else:
            print(number)
            
