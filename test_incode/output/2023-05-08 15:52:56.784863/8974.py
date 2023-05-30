#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that adds numbers.
    httpd = HTTPServer(("", 80), NumbersHandler)
    httpd.serve_forever()

