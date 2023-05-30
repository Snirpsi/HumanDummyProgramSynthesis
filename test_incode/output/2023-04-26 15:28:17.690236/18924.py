#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or returns fruits. """    
    
    port = int(sys.argv[1])
    fruits = convert_port(port)
    
    print("Fruits:")
    for fruit in fruits:
        print(