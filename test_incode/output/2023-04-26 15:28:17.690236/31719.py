#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    port = 8080
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('serving at port', port)
    httpd.serve_forever()
