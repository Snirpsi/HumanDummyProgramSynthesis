#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or calculates user input. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            break
        else:
            print('Your port number is', port)
            
