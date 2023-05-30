#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    
    port = sys.argv[1]
    
    httpd = HTTPServer(("", port), MyHandler)
    
    print("Serving HTTP on port " + port)
    httpd.serve_forever()
    
