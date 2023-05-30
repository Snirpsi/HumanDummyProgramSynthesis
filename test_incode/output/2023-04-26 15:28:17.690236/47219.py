#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits or iterates over a port. """    
    port = int(sys.argv[1])
    fruit = Fruit(port)
    fruit.open()
    fruit.iter