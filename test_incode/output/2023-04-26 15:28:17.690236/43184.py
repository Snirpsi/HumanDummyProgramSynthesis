#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or opens words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsServer)
    
    server.serve_forever()
    
