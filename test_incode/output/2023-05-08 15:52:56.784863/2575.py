#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that removes numbers.
    server = HTTPServer(("", 80), NumbersHandler)
    server.serve_forever()

