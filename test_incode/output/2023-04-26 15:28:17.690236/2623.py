#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and adds a list of words. """    
    
    port = int(sys.argv[1])
    words = []
    
    for word in sys.argv[2:]:
        words.append(word)
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
