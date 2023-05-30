#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), NumberConverter)
    
    print("Serving at port " + str(port))
    
    server.serve_forever()
    
