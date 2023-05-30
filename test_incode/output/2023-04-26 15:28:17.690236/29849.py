#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or iterates over a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), NumbersHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
    
