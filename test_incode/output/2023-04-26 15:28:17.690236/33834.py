#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(-1)
    
    port = int(sys.argv[1])
    
    from gevent import monkey
    monkey.patch_all()
    
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket.server import WebSocketServer
    
    server = WebSocketServer(
        ('/ws', WebSocketHandler),
        