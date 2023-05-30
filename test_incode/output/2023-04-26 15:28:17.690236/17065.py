#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and returns words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port {}...'.format(port))
    
    httpd.serve_forever()
    
