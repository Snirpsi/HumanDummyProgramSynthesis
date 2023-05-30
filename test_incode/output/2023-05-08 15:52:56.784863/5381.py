#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that iterates over numbers.
    #It will serve the numbers from 1 to 3 as static files.
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

