#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import os
    
    port = int(os.getenv('PORT', 8080))
    
    