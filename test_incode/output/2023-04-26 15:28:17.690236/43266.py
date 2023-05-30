#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    from gevent import monkey
    monkey.patch_all()
    
    from gevent.wsgi import WSGIServer
    
    server = WSGIServer(('', 80), app)
    
    server.serve_forever()
    
