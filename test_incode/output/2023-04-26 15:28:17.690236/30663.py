#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or multiplyes numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
