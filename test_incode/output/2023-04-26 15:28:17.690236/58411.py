#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or removes a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
    
