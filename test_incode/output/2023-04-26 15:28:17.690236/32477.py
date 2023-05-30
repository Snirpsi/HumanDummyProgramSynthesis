#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    from gevent import monkey
    monkey.patch_all()
    from gevent.wsgi import WSGIServer
    
    server = WSGIServer(('localhost', 8080), WordsHandler)
    server.serve_forever()
    
