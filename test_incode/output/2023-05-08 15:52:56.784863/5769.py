#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that prints numbers.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

