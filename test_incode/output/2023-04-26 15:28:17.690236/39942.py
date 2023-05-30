#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or removes user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
    
