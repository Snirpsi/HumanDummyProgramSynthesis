#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that returns a port.
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

