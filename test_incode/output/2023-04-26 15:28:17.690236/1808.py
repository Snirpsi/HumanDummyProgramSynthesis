#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or stores fruits. """    
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_store = FruitStore(fruits)
    
    fruits_store.store()
    
    fruits_store.close()
    
    port = fruits_store.port
    
    print('Serving on port {}'.format(port))
    
    httpd = make_server('', port, FruitHandler)
    
    httpd.serve_forever()
    
