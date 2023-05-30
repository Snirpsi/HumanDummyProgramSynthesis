#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and stores words. """    
    
    words = []
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    print('Starting server...')
    httpd.serve_forever()
    
    print('Stopping server...')
    httpd.socket.close()
    
    print('Done.')
    
