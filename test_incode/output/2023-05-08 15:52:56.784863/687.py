#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.txt and prints its contents
    from http.server import BaseHTTPRequestHandler, HTTPServer
    httpd = HTTPServer(('', 8000), MyHandler)
    print('Serving on port 8000...')
    httpd.serve_forever()

