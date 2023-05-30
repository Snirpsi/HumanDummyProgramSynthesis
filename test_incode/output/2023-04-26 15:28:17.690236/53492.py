#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port and prints a list of numbers. """    
    
    ports = []
    
    for x in range(1,10):
        ports.append(x)
    
    for x in range(1,10):
        if x not in ports:
            print("Port {} is not in list".format(x))
            
        else:
            print("Port {} is in list".format(x))
            
