#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that returns numbers.
    #It can be run from the command line with python -m http.server
    import sys
    import http.server
    import socketserver

    HOST, PORT = "localhost", 8000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    print("Serving at http://%s:%s" % (HOST, PORT))
    httpd.serve_forever()

