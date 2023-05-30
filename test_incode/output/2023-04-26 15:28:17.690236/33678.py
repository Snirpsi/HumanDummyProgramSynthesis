#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or enumerates a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
