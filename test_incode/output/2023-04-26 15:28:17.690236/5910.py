#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and returns user input. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), RequestHandler)
    
    server.serve_forever()
    
