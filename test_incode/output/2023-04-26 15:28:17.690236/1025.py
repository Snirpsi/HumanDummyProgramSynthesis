#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and removes user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), RequestHandler)
    
    server.serve_forever()

<|/ file ext=.py filename=