#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    #It can be run from the command line or as a script.
    import sys
    web = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    web.serve_forever()

