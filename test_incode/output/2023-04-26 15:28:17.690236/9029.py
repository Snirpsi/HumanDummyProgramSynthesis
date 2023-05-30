#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or returns a port. """    
    
    port = int(sys.argv[1])
    
    if sys.argv[2:]:
        numbers = sys.argv[2:]
    else:
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    numbers_