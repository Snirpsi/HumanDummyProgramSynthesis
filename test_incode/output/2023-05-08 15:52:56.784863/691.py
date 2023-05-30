#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens a list of words.
    import sys
    import socketserver
    HOST, PORT = "localhost", 8000
    Handler = socketserver.BaseRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    httpd.serve_forever()

