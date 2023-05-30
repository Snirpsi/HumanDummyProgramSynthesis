#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or converts fruits. """    
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
