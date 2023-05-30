#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers and returns words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsServer)
    