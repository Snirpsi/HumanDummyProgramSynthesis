#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or converts words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitServer)
    httpd.serve_forever()
    
