#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    from gevent import monkey
    monkey.patch_all()
    from geventwebsocket.handler import WebSocketHandler
    server = WebSocketHandler