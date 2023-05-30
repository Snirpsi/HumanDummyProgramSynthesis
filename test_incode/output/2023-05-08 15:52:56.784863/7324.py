#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that returns numbers.
    web = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    web.serve_forever()

