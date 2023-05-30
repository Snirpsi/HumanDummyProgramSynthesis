#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and stores fruits. """    
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'banana', 'cherry', 'orange', 'pear']
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('serving at port ' + str(port))
    
    server.serve_forever()
    
