#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports and multiplyes a list of numbers. """    
    ports = [1,2,3,4,5,6,7,8,9,10]
    ports_multiplied = [x*y for x,y in zip(ports,ports)]
    print(ports_multiplied)
    
