#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and stores all ports. """    
    from gevent import monkey
    monkey.patch_all()
    from geventwebsocket.handler import WebSocketHandler
    
    server = WebSocketHandler()
    server.serve_forever()