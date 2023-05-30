#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and opens user input. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
