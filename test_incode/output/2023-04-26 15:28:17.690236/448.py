#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and adds fruits. """    
    port = int(sys.argv[1])
    fruits = ['apple', 'orange', 'banana', 'pear']
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('serving at port ' + str(port))
    
    server.serve_forever()
    
