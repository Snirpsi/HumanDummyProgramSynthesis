#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that opens a list of numbers.
    web = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    web.serve_forever()

