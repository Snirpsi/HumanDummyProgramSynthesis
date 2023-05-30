#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or adds numbers. """    
    
    words = ['word1', 'word2', 'word3', 'word4']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsHandler)
    httpd.serve_forever()
    
