#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or converts a port. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            print('Invalid port number')
        else:
            break
        
    print('The port number you entered is ' + str(port))
    
