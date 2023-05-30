#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that requests ports.
    while True:
        for port in ports:
            httpd = HTTPServer(('', port), Handler)
            print('Serving HTTP on port %s' % port)
            httpd.serve_forever()

