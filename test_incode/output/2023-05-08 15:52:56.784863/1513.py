#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that prints user input.
    import sys
    web = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    web.serve_forever()

