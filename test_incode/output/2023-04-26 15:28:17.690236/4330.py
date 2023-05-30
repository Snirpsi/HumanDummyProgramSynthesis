#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    words = ['word1', 'word2', 'word3']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
