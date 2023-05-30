#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    httpd = HTTPServer(("", 80), WordsHandler)
    httpd.serve_forever()
    
