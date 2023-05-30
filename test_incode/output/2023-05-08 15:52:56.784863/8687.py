#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that returns a list of numbers.
    #The server can be run from the command line or by calling this script from the command line.
    webserver = WebServer()
    webserver.serve_forever()

