#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or opens fruits. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    httpd = HTTPServer(("", port), FruitHandler)
    httpd.serve_forever()
    
