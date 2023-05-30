#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and converts a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Starting server on port ' + str(port) + '...')
    httpd.serve_forever()
    
