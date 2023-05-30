#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that converts a port.
    web = HTTPServer(('', port), Handler)
    web.serve_forever()

