#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that stores numbers.
    server = HTTPServer(('', 8000), NumberServer)
    server.serve_forever()

