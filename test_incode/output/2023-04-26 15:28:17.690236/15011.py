#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or prints user input. """    
    port = int(input('Enter a port number: '))
    
    for port in range(port):
        print('Enter your port number:', port)
        
