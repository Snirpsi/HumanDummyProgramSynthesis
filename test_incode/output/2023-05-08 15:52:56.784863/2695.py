#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them.
    import os
    import http.server
    import socketserver

    HOST, PORT = "localhost", 8000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    print("serving at http://%s:%s" % (HOST, PORT))
    httpd.serve_forever()

