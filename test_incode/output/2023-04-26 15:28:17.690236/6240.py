#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    import os
    import http.server
    import socketserver
    import argparse
    
    parser = argparse.ArgumentParser(description='A minimal webserver that removes a list of words')
    parser.add_argument('words', metavar='words', nargs='+', help='words to remove')
    args = parser.parse_args()
    
    words = [word.strip() for word in args.words]
    
    httpd = socketserver.TCPServer(('localhost', 80), http.server.SimpleHTTPRequestHandler)
    httpd.