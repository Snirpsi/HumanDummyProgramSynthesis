#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and prints a list of words. """    
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), WordsServer)
    server.serve_forever()
    
    
