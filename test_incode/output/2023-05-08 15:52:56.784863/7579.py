#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that stores a port.
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()

