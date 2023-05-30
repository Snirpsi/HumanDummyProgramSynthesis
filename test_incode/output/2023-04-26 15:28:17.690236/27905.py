#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and enumerates fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = []
    
    for i in range(port):
        fruits.append(i)
        
    for fruit in fruits:
        print("Fruit 