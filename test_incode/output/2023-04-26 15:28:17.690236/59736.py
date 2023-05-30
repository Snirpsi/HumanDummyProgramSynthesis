#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or adds numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
