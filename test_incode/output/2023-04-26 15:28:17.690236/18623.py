#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    from gevent import monkey
    monkey.patch_all()
    from gevent.wsgi import WSGIServer
    server = WSGIServer(('0.0.0.0', 8080), app)
    server.serve_forever()
