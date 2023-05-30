#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), UserInputHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
    
