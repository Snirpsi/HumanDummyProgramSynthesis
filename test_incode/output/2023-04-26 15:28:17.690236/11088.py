#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and iterates over user input. """    
    port = int(input("Enter a port number: "))
    
    # iterate over user input
    for port in ports:
        print("The port number {} multiplied by {} is {}".format(port, port, port * port))
    
