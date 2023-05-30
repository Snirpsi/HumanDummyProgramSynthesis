#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    port = sys.argv[1]
    
    webserver = HTTPServer(('', port), WordsHandler)
    webserver.serve_forever()
