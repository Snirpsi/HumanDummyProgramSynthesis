#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    words = ['hello', 'world']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port 