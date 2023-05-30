#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    words = ['word1', 'word2']
    
    httpd = HTTPServer(('', 8080), WordsHandler)
    httpd.serve_forever()
    
    
