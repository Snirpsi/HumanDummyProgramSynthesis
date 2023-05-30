#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    words = ['word1', 'word2', 'word3', 'word4']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port %s' % port)
    
    httpd.serve_forever()
    
