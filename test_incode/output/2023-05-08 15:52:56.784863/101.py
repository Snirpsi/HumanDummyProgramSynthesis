#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that adds numbers.
    web = HTTPServer(('', 8080), NumberHandler)
    web.serve_forever()

