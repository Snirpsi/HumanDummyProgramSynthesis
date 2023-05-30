#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    from fruit import Fruit
    
    server = Fruit()
    
    server.serve()
    
