#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and iterates over user input. """    
    
    port = int(input("Enter a port number: "))
    
    for port in range(port):
        
        print("Port number {} is {}".format(port, 