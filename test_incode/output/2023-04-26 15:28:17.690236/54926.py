#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import os
    
    port = int(os.getenv('PORT', 8080))
    
    web