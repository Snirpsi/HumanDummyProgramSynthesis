#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and iterates over a list of words. """    
    
    port = int(sys.argv[1])
    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
