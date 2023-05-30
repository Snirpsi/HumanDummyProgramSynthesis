#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that stores all ports.
    server = HTTPServer(('',8080), Handler)
    server.serve_forever()

