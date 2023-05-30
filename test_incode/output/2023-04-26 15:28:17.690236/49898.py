#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    from gevent import monkey
    monkey.patch_all()
    from geventwebsocket.handler import WebSocketHandler
    
    server = WSGIServer(('', 80), WebSocketHandler)
    server.serve_forever()
