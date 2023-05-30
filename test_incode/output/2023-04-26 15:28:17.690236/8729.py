#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or multiplyes user input. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
