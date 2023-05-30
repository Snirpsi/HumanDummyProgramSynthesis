#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers and returns user input. """    
    while True:
        number = int(input('Enter a number: '))
        
        if number > 100:
            print('Too high!')
        elif number < 1:
            print('Too low!')
        else:
            print('You entered a number!')
            
