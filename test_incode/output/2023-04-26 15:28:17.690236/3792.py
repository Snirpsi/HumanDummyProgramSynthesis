#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and stores a port. """    
    
    port = int(sys.argv[1])
    
    words = ["word1", "word2"]
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
