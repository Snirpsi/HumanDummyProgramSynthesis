#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that returns numbers.
    webserver = HTTPServer(("", 80), NumberHandler)
    webserver.serve_forever()

