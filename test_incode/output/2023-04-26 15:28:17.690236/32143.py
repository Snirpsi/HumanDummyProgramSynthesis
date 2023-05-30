#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    port = 8080
    
    httpd = HTTPServer(("", port), Handler)
    print("Serving on port {}".format(port))
    httpd.serve_forever()
