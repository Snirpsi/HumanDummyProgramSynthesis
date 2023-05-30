#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    words = ['cat', 'dog', 'mouse']
    
    port = 5000
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Starting web server on port ' + str(port) + '...')
    httpd.serve_forever()
    
