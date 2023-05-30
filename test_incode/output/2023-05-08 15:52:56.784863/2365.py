#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that adds all ports.
    server = HTTPServer(('',0), Handler)
    server.serve_forever()

