#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that enumerates a list of numbers.
    import sys
    port = int(sys.argv[1])
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()

