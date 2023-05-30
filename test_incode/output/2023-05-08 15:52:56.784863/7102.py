#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that calculates numbers.
    httpd = HTTPServer(("", 80), NumberCalculator)
    httpd.serve_forever()

