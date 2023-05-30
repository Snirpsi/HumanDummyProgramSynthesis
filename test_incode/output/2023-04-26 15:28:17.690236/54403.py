#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port and converts fruits. """    
    
    port = int(sys.argv[1])
    fruits = sys.argv[2:]
    
    remove_port(port)
    
    for fruit in fruits:
        convert_fruit(fruit)
        
