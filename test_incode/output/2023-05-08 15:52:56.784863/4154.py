#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that adds a port.
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('serving at port', port)
    httpd.serve_forever()

