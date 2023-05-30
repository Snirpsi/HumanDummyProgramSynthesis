#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that adds ports.
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()

