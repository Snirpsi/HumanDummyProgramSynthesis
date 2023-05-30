#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    import os
    
    os.chdir('fruits')
    
    import web
    
    app = web.application(urls, globals())
    
    web.