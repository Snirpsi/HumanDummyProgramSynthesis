#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    import http.server
    import socketserver
    
    HOST, PORT = "localhost", 8000
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    print("Starting web server on port 8000")
    httpd.serve_forever()
    
