#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that prints numbers.
    import sys
    port = sys.argv[1]
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()

