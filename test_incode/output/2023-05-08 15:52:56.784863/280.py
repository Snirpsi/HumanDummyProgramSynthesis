#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that iterates over ports.
    for port in ports:
        server = HTTPServer(('', port), Handler)
        print('Serving on port {}'.format(port))
        server.serve_forever()

