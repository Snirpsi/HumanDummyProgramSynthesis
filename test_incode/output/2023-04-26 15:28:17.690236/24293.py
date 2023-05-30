#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    httpd.serve_forever()
