#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that requests a port.
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()

