#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and opens all ports. """    
    
    port = int(sys.argv[1])
    
    words = ['word1', 'word2', 'word3']
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Starting server on port %d...' % port)
    httpd.serve_forever()
    
