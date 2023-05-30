#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or returns a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()
    
