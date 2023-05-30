#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that returns all ports.
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()

