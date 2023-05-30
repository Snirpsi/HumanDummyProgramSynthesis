#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    server = HTTPServer(('localhost', port), WordsHandler)
    
    server.serve_forever()
    
    
