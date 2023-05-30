#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that iterates over ports.
    for port in ports:
        httpd = HTTPServer(('', port), Handler)
        print('Serving on port ' + str(port))
        httpd.serve_forever()

