#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or returns user input. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            port = '-1'
        else:
            port = int(port)
        
        if port > 0 and port < 65535:
            print("Port number {} is open".format(port))
        else:
            print("Port number {} is not open".format(port))
    
