#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    import sys
    from gevent import monkey
    monkey.patch_all()
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket import WebSocket
    
    server = WebSocketHandler()
    
    port = int(sys.argv[1])
    
    server.serve_forever()
    
