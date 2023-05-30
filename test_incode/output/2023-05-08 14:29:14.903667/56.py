#!/usr/bin/python3
ports = range(0,65534)
if __name__ == '__main__':
    #A minimal webserver that returns ports.
    httpd = HTTPServer(('', 80), Handler)
    httpd.serve_forever()

