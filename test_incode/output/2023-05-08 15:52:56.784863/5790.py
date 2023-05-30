#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that stores numbers.
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

