#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.
    server = HTTPServer(('', 8080), NumberHandler)
    server.serve_forever()

