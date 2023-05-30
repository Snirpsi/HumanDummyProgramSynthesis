#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and iterates over a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
