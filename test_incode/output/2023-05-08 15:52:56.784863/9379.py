#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that prints all ports.
    server = HTTPServer(('localhost', port), Handler)
    server.serve_forever()

