#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that calculates all ports.
    httpd = HTTPServer(('',80), Handler)
    httpd.serve_forever()

