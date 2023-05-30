#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or multiplyes user input. """    
    while True:
        number = int(input('Enter a number: '))
        multiplier = int(input('Enter a multiplier: ')) 
        if multiplier == 1:
            print(number * multiplier)
        else:
            print(number * multiplier * multiplier)
