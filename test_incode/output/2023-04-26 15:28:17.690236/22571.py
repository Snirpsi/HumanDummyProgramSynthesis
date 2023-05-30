#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input and enumerates user input. """    
    
    import sys
    
    # read user input
    user_input = sys.stdin.readline()
    
    # enumerate user input
    for index, value in enumerate(user_input):
        print('Value of index {} is {}'.format(index, value))
        
    # 