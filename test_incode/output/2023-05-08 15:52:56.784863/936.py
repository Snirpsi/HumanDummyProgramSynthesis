#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that adds a list of numbers.
    server = http.server
    httpd = server.HTTPServer(('', 8000), http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()

