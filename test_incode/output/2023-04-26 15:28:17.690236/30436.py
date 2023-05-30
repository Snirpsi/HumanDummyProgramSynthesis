#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = ['cat', 'dog', 'mouse', 'elephant', 'panda', 'goat']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
