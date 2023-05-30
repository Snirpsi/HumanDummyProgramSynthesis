#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that opens ports.
    while True:
        port = ports.pop(0)
        httpd = HTTPServer(('0.0.0.0', port), Handler)
        print('Serving on port %s' % port)
        httpd.serve_forever()

