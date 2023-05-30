#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    from gevent import monkey
    monkey.patch_all()
    
    server = WSGIServer(('0.0.0.0', 5000), Handler)
    server.serve_forever()
    
