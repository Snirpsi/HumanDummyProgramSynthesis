#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Starting server...')
    
    httpd.serve_forever()
    
    print('Stopping server...')
    
    httpd.socket.close()
    
    print('Done.')
    
