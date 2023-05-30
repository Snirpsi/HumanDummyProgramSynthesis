#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or multiplyes fruits. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, FruitServer)
    
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
