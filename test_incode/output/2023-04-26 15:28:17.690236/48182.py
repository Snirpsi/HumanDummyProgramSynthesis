#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    import sys
    from gevent import monkey
    monkey.patch_all()
    from geventwebsocket.handler import WebSocketHandler
    application = WebSocketHandler(