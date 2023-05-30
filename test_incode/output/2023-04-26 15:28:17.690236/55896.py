#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and enumerates words. """    
    import sys
    from gevent import monkey
    monkey.patch_all()
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket import WebSocketServer
    
    server = WebSocketServer(('localhost', 8080), WebSocketHandler)
    server.serve_forever()

<|/ file source=github ext=.py |>