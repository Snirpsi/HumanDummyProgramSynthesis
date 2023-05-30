#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and adds fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'banana', 'cherry']
    
    numbers = [int(n) for n in sys.argv[2:]]
    
    numbers += fruits
    
    print('\n'.join(map(str, numbers)))
    
    print('Serving on port %s' % port)
    
    httpd = HTTPServer(('', port), FruitServer)
    httpd.serve_forever()
    
