#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
    
