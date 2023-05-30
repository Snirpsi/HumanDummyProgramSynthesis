#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %d" % port)
    
    httpd.serve_forever()
    
