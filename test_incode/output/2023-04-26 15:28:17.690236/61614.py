#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or adds user input. """    
    
    ports = enumerate()
    
    for port in ports:
        print("Port {} is open".format(port))
        
    while True:
        port = input("Enter a port number: ")
        if port in ports:
            print("Port {} is open".format(port))
        else:
            print("Port {} is not open".format(port))
            
