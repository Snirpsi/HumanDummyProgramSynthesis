#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that stores numbers.
    #This script is intended to be run from the command line.
    #It will serve the numbers from numbers.txt.
    server = HTTPServer(('', 8000), NumbersHandler)
    server.serve_forever()

