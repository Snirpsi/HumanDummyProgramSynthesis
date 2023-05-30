#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or returns a port. """    
    
    port = int(sys.argv[1])
    
    if port > 65535:
        print("Port must be <= 65535")
        exit(1)
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
