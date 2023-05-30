#!/usr/bin/python3
ports = range(0,65534)
if __name__ == '__main__':
    #A minimal webserver that prints ports.
    httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    httpd.serve_forever()

