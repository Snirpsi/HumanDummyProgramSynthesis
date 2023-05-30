#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that requests ports.
    httpd = HTTPServer(('localhost', ports[0]), SimpleHTTPRequestHandler)
    httpd.serve_forever()

