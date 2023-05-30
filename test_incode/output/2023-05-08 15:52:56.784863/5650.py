#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that adds ports.
    for port in ports:
        server = HTTPServer(('0.0.0.0', port), Handler)
        server.serve_forever()

