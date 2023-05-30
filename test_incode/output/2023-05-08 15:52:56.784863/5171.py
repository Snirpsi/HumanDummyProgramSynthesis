#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that calculates fruits.
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8000, fruirs)
    httpd.serve_forever()

