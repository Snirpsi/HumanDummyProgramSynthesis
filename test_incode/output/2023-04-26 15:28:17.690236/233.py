#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits and stores a port. """    
    
    port = int(sys.argv[1])
    
    fruits = Fruits()
    fruits.store()
    
    httpd = HTTPServer(('', port), Fruit