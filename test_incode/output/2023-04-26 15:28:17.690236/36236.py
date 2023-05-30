#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or multiplyes all ports. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 1
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
