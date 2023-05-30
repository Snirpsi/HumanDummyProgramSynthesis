#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), RemoveWordsHandler)
    
    server.serve_forever()
    
