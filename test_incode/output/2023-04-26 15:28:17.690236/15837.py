#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or calculates user input. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        print('The port number is', port)
        
    
<|/ file ext=.py filename=