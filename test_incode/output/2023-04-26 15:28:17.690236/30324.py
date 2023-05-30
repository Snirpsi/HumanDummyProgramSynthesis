#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or prints fruits. """    
    
    port = int(sys.argv[1])
    
    fruits = convert_fruits(port)
    
    for fruit in fruits:
        print(