#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or adds words. """    
    while True:
        multiplier = int(input('Enter a number: '))
        if multiplier == 0:
            break
        else:
            print('The product of %d and %d is %d.' % (multiplier, multiplier, multiplier * multiplier))
