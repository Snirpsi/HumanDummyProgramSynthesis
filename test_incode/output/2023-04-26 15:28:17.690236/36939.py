#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    numbers = [int(x) for x in words]
    
    print('\n'.join(str(x) for x in numbers))
    
