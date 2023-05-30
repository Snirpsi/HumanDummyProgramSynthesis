#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    import os
    
    port = int(os.environ.get('PORT', 8080))
    
    webserver_