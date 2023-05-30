#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    port = 8080
    
    httpd = HTTPServer(("", port), Handler)
    print("Serving on port " + str(port))
    httpd.serve_forever()
