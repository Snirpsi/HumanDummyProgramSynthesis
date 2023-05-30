#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    import sys
    from gevent import monkey
    monkey.patch_all()
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket.server import WebSocketServer
    
    server = WebSocketServer(('0.0.0.0', 8080), WebSocketHandler)
    server.serve_forever()
