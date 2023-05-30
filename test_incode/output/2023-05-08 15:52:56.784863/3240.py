#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that returns fruits.
    httpd = HTTPServer(('', 8080), FruitHandler)
    httpd.serve_forever()

