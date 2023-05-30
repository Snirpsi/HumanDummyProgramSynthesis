#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    import socketserver
    import math
    
    HOST, PORT = 'localhost', 8080
    
    Handler = socketserver.BaseRequestHandler
    
    class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        pass
    
    server = ThreadedTCPServer((HOST, PORT), Handler)
    
    server.serve_forever()
    
    
