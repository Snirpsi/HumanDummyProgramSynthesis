#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    #This example is intended for educational purposes.
    #It is not intended for production use.
    import sys
    import os
    import http.server
    import socketserver
    import webbrowser
    import argparse
    
    parser = argparse.ArgumentParser(description='A minimal webserver that returns user input.')
    parser.add_argument('-p', '--port', default=8000, type=int, help='port to listen on')
    parser.add_argument('-n', '--no-open', action='store_true', help='do not open a browser window')
    args = parser.parse_args()
    
    httpd = socketserver.TCPServer(("", args.port), http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()

