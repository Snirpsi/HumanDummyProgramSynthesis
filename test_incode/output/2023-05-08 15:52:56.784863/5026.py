#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that converts all ports.
    httpd = HTTPServer(('', 80), MyHandler)
    httpd.serve_forever()

