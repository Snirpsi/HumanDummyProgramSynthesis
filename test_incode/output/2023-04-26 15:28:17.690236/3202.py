#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers and enumerates a port. """    
    ports = [
        (i, i+1) for i in range(1,65535)
    ]
    
    for port, number in ports:
        print("Port {} is {} and has {} connections.".format(port, number, len(port)))
    
    print("\n