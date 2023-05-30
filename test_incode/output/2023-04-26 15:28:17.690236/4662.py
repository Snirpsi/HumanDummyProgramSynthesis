#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or opens user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    print("Serving on port %d" % port)
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
