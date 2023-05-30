#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.abspath('..'))
    
    from fruits import Fruits
    
    fruits = Fruits()
    
    port = int(sys.argv[1])
    
    fruits.listen(port)
    
    