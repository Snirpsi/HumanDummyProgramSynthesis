#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and opens user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving at port %d" % port)
    
    server.serve_forever()
    
