#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    import sys
    import os
    port = int(sys.argv[1])
    web = HTTPServer(("", port), SimpleHTTPRequestHandler)
    web.serve_forever()

