#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that adds a list of numbers.
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()

