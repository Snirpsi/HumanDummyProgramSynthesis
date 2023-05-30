#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    print("Serving at port %d" % port)
    
    server.serve_forever()
    
