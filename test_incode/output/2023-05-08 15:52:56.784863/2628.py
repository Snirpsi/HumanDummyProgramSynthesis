#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in a
    #browser
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server = HTTPServer(('', 8000), BaseHTTPRequestHandler)
    
    #This line is required to run this script from the command line
    server.serve_forever()

