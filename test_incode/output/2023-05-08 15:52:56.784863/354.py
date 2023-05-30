#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    httpd = HTTPServer(('localhost', port), Handler)
    httpd.serve_forever()

