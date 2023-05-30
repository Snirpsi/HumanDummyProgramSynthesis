#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that prints a list of numbers.
    webserver = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    webserver.serve_forever()

