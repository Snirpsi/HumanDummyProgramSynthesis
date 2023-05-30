#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and enumerates fruits. """    
    
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: %s <port> <fruits>" % sys.argv[0])
        exit(1)
    
    port = sys.argv[1]
    fruits = sys.argv[2]
    
    fruit = fruits.split(',')
    
    fruits.sort()
    
    for fruit in fruit:
        print("%s: %s" % (fruit, port))
    
    exit(0)

<|/ file filename=fruits.py ext=.py |>