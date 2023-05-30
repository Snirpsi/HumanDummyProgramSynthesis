#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    words = ['word1', 'word2']
    
    port = 5000
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port %s' % port)
    
    httpd.serve_forever()
    
