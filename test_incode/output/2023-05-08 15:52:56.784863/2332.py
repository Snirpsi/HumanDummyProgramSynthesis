#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that enumerates ports.
    for port in ports:
        server = HTTPServer(('', port), Handler)
        server.serve_forever()

