#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and returns a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving on port {}".format(port))
    
    server.serve_forever()
    
