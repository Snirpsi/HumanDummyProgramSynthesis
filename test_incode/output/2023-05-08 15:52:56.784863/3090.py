#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that removes a list of numbers.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

