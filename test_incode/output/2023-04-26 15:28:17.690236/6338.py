#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    
    from fruits import Fruits
    
    fruits = Fruits()
    
    port = int(sys.argv[1])
    
    fruits.serve(port)
    
