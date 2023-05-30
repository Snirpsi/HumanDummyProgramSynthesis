#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port or calculates user input. """    
    port = int(input('Enter a port number: '))
    
    if port > 65535:
        print('Sorry, your port number is too large.')
        
    else:
        print('Your port number is ' + str(port))
    
