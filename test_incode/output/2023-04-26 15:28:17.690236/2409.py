#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or prints all ports. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
    
