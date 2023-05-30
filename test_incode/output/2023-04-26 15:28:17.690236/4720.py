#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints fruits or iterates over a port. """    
    
    port = int(sys.argv[1])
    
    if port == -1:
        port = 0
    
    fruit = Fruit(port)
    
    while True:
        fruit.