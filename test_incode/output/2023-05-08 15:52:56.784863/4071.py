#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that iterates over a port.
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

