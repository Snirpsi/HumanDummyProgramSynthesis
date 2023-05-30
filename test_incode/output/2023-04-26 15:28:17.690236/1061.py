#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and multiplyes a port. """    
    port = int(sys.argv[1])
    words = list(map(int, sys.argv[2:]))
    
    server = HTTPServer(('', port), WordsServer)
    
    