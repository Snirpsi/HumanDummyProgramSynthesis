#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or prints fruits. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()
