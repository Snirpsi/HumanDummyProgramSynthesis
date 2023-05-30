#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that returns numbers.
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()

