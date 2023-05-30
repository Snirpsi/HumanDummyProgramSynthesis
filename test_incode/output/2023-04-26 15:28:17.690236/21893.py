#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers and prints fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()
    
