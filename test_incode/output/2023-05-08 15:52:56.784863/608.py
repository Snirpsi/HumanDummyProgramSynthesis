#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that calculates numbers.
    server = HTTPServer(('', 8000), NumberHandler)
    print('Starting server')
    server.serve_forever()

