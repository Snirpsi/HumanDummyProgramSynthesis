#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that stores user input.
    #This script is intended to be run from the command line.
    import sys
    import os
    
    port = 8080
    
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()

