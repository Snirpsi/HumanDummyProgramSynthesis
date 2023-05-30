#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers and multiplyes user input. """    
    while True:
        number = int(input('Enter a number: '))
        multiplier = int(input('Enter a multiplier: ')) 
        number *= multiplier
        print(number)
