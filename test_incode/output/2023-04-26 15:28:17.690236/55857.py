#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 1000:
            print('Too high!')
        else:
            print('You entered a number!')
            break
        
    print('Ended the loop')
    
