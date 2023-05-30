#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.txt and displays them in HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from os.path import join, dirname
    import os
    import sys
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

