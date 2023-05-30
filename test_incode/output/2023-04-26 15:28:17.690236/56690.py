#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or prints fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        fruits = sys.argv[1:]
    else:
        fruits = ['apple', 'orange', 'banana', 'cherry']
    
    print('\n'.join(