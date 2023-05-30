#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    print('Serving at port ' + str(port) + '...')
    
    httpd.serve_forever()
    
