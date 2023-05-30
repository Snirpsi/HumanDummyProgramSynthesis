#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    words = ['word1', 'word2']
    
    port = 5000
    
    httpd = HTTPServer(("", port), WordsHandler)
    
    print("Serving WordsHandler on port {}".format(port))
    httpd.serve_forever()
    
