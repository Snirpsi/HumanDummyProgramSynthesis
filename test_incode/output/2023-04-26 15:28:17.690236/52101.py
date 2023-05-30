#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or removes user input. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), Handler)
    print("Serving at port", port)
    server.serve_forever()
