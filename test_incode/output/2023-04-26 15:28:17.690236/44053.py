#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = ['word1', 'word2', 'word3']
    
    server = HTTPServer(('', 8080), WordsHandler)
    
    print('Starting server')
    server.serve_forever()
    
