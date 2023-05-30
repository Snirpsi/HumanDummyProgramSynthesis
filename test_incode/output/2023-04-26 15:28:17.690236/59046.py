#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    words = ['word1', 'word2', 'word3']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsHandler)
    
    print("Serving on port {}".format(port))
    httpd.serve_forever()
    
