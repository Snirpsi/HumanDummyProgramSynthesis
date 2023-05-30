#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.
    server = HTTPServer(('localhost', 8000), NumberHandler)
    server.serve_forever()

