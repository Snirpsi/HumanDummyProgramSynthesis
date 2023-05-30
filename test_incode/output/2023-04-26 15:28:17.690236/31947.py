#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import os
    import socketserver
    
    HOST, PORT = 'localhost', 8000
    
    Handler = socketserver.BaseRequestHandler
    
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    print("Serving on port {}".format(PORT))
    
    httpd.serve_forever()
    
