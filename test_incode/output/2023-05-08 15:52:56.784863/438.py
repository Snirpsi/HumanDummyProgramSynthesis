#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.txt and displays them in index.html
    import os
    import sys
    webserver_address = ('localhost', 8000)
    webserver = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    webserver.serve_forever()

