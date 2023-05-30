#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or returns fruits. """    
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
