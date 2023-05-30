#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    fruits = ['apple', 'banana', 'cherry', 'pear', 'orange', 'mango', 'pineapple', 'plum']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    print("Serving at port %d" % port)
    
    server.serve_forever()
    
