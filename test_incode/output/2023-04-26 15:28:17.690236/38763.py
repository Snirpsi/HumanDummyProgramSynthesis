#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and calculates a port. """    
    
    ports = [
        8080,
        8081
    ]
    
    for port in ports:
        print("Port {} is open".format(port))
        
