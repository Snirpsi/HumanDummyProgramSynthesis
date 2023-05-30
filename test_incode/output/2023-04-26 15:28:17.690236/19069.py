#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and opens a port. """    
    
    words = []
    
    port = 5000
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Serving at port %s' % port)
    
    httpd.serve_forever()
    
