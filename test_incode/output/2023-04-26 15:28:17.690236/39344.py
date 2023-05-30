#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving at port %d" % port)
    httpd.serve_forever()
