#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    #It also prints out the user input to the console.
    import sys
    import os
    webserver = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    webserver.serve_forever()

