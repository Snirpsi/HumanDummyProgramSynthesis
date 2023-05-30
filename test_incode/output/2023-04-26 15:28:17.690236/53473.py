#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or converts user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), RequestHandler)
    
    print("Serving at port", port)
    
    server.serve_forever()
    
