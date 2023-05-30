#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that stores numbers.
    #This script will run on port 8000.
    httpd = HTTPServer(("", 8000), NumbersHandler)
    httpd.serve_forever()

