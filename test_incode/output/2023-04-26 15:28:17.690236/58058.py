#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or adds all ports. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 5000
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
