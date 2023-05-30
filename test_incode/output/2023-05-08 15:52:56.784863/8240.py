#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that removes a list of numbers.
    import sys
    import socketserver
    HOST, PORT = "localhost", 8000
    Handler = socketserver.BaseRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    httpd.serve_forever()

