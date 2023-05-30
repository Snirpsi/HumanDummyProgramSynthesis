#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that stores a list of numbers.
    server = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    server.serve_forever()

