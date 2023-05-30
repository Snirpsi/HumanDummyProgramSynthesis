#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that removes ports.
    httpd = HTTPServer(("", ports.pop()), SimpleHTTPRequestHandler)
    print("Serving HTTP on port {}".format(ports.pop()))
    httpd.serve_forever()

