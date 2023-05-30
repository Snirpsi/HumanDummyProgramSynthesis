#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers and removes a port. """    
    ports = [1,2,3,4,5,6,7,8,9,10]
    for port in ports:
        if port % 2 == 0:
            print(port)
        else:
            print(port-1)
            
