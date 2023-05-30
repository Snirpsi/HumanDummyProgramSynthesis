#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    import os
    
    port = int(os.environ.get('PORT', 8080))
    
    from tornado.wsgi import WSGIContainer
    
    container = WSGIContainer(