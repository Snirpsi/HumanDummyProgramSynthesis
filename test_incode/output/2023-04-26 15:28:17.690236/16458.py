#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python number_to_list.py <number_list>')
        exit(1)
    
    number_list = sys.argv[1:]
    
    number_to_list(number_list)
    
