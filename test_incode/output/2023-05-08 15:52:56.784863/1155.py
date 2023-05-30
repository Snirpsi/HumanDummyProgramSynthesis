#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that prints a list of numbers.
    server = BaseHTTPServer.HTTPServer(('localhost', 8000), MyHandler)
    server.serve_forever()

