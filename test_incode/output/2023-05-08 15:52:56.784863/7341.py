#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that enumerates ports.
    while True:
        for port in ports:
            print("Starting port {} ...".format(port))
            httpd = HTTPServer(('', port), Handler)
            httpd.serve_forever()
        print("Stopping port {} ...".format(port))
        httpd.server_close()

