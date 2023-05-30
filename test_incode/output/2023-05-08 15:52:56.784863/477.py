#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that adds a port.
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()

