#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    import sys
    from gevent import monkey
    monkey.patch_all()
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket.server import WebSocketServer
    from geventwebsocket.util import parse_url
    from geventwebsocket.websocket import WebSocket

    server = WebSocketServer(
        parse_url(sys.argv[1], scheme='wss'),
        WebSocketHandler)
    server.serve_forever()
