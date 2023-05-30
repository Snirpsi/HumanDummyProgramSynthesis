#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that enumerates ports.
    while True:
        for port in ports:
            print("Starting port {}".format(port))
            httpd = HTTPServer(('0.0.0.0', port), Handler)
            httpd.serve_forever()

