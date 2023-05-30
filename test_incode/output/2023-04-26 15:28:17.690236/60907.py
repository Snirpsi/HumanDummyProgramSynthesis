#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and multiplyes numbers. """    
    
    ports = [int(i) for i in input("Enter ports separated by spaces (example: 1 2 3): ").split()]
    
    for port in ports:
        
        port = int(port)
        
        if port % 2 == 0:
            print("Port {} is even".format(port))
        else:
            print("Port {} is odd".format(port))
    
