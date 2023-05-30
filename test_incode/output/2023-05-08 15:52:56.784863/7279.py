#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.txt and prints them out
    httpd = HTTPServer(('localhost', 8000), NumbersHandler)
    httpd.serve_forever()

