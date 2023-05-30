#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that stores a port.
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port {}'.format(port))
    httpd.serve_forever()

