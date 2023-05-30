#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or prints fruits. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), FruitHandler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()
