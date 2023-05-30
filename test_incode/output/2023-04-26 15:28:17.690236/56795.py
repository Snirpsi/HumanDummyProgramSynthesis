#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
