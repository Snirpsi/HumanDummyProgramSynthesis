#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and returns a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()
