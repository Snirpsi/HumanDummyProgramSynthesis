#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and enumerates words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Starting server on port ' + str(port) + '...')
    httpd.serve_forever()
    
