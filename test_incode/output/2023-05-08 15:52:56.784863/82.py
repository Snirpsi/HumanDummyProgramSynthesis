#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that requests a list of numbers.
    server = HTTPServer(('', 8000), RequestHandler)
    server.serve_forever()

