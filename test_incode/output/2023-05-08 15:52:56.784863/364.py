#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that requests a port.
    while True:
        port = port + 1
        httpd = make_server('localhost', port, app)
        httpd.serve_forever()

