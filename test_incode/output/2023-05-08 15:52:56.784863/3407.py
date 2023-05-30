#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that iterates over numbers.
    import sys
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, MyHandler)
    httpd.serve_forever()

