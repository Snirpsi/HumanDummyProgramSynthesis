#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or iterates over a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    if port > 0:
        words = [w for w in open('words.txt')]
        
    
    if port > 0:
        server = HTTPServer(("", port), WordsHandler)
        server.serve_forever()
        
    else:
        server = HTTPServer(("", 80), WordsHandler)
        server.