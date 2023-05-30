#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or adds a list of numbers. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8000
        
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
