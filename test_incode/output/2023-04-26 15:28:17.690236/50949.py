#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Starting server')
    httpd.serve_forever()
    
    
