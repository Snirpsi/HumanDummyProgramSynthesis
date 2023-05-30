#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    print('Serving HTTP on port 8080')
    httpd.serve_forever()
