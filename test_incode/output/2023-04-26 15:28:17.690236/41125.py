#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or prints words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    