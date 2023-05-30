#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that removes all ports.
    webserver = HTTPServer(('', 0), Handler)
    webserver.serve_forever()

