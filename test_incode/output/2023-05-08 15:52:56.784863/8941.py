#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that stores ports.
    server = HTTPServer(('',80), Handler)
    server.serve_forever()

