#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and opens fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), FruitHandler)
    httpd.serve_forever()
