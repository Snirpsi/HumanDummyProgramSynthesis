#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and adds numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
