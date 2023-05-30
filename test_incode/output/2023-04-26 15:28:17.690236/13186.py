#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or multiplyes a list of numbers. """    
    import sys
    import socketserver
    
    HOST, PORT = sys.argv[1], int(sys.argv[2])
    
    Handler = socketserver.BaseRequestHandler
    
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    print("Serving HTTP on", HOST, PORT)
    
    httpd.serve_forever()
    
