#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    import sys
    import os
    import http.server
    import socketserver
    import webbrowser
    import argparse
    
    parser = argparse.ArgumentParser(description="A minimal webserver that prints a list of words.")
    parser.add_argument("words", help="words to print")
    args = parser.parse_args()
    
    words = [word.strip() for word in args.words.split(',')]
    
    httpd = socketserver.TCPServer(("", 80), http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
    webbrowser.open("http://localhost:80/", new=2)
    
