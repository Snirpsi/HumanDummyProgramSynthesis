#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that adds a port.
    server = HTTPServer(('', port), Handler)
    server.serve_forever()

