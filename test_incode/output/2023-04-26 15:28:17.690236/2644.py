#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or returns user input. """    
    
    # read user input
    number = int(input('Enter a number: '))
    
    # multiply number
    result = number * 2
    
    # print result
    print('The product of {} and {} is {}.'.format(number, number, result))
    
    # exit program
    exit()
    
# 