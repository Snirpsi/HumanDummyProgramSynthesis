#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or multiplyes numbers. """    
    
    import os
    
    port = int(os.environ.get('PORT', 5000))
    
    web