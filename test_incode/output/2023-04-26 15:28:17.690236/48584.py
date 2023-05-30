#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port {}'.format(port))
    
    httpd.serve_forever()
    
