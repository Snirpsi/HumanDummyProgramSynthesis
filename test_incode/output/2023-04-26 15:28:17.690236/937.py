#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    import sys
    from gevent.wsgi import WSGIServer
    from geventwebsocket.handler import WebSocketHandler
    
    server = WSGIServer(('0.0.0.0', 8080), WebSocketHandler)
    server.serve_forever()
    
