#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    from fruits import Fruits
    
    fruits = Fruits()
    
    port = int(sys.argv[1])
    
    