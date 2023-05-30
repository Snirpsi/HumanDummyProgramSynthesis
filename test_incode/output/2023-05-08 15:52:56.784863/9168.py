#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that prints numbers.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    httpd = HTTPServer(('', 8000), MyHandler)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()

