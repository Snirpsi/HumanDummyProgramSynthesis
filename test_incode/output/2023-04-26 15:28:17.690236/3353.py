#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and converts all ports. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

<|/ file ext=.py filename=