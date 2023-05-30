#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that requests a port.
    while True:
        port = 8080
        httpd = HTTPServer(('', port), RequestHandler)
        httpd.serve_forever()

