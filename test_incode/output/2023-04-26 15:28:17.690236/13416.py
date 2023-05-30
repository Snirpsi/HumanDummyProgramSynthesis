#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    import sys
    port = sys.argv[1]
    
    from gevent import monkey
    monkey.patch_all()
    
    from geventwebsocket.handler import WebSocketHandler
    
    server = WebSocketHandler()
    
    server.serve_forever()
    
