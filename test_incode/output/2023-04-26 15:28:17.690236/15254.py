#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import os
    
    port = int(os.environ.get('PORT', 8080))
    
    web = 