#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port or prints numbers. """    
    import sys
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        print('Port number is', port)
    else:
        print('Enter a port number')
