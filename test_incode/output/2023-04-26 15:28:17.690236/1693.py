#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or prints fruits. """    
    
    port = int(sys.argv[1])
    
    for fruit in fruits(port):
        print(fruit)
        
