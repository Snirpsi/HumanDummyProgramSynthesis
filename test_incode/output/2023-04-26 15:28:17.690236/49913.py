#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Starting web server on port ' + str(port) + '...')
    httpd.serve_forever()
    
