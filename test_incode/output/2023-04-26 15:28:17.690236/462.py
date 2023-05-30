#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Starting web server on port %s' % port)
    httpd.serve_forever()
    
