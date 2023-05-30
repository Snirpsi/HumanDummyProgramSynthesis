#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    webdir = os.path.join('..', 'web')
    
    webapp = web.application(urls, globals())
    
    webapp.add_