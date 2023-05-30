#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that adds numbers.
    webserver = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    webserver.serve_forever()

