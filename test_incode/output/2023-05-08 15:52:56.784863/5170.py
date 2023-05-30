#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that enumerates a list of numbers.
    webserver_address = ('localhost', 8000)
    webserver = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    webserver.serve_forever()

