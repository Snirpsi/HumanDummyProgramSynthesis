#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    port = int(sys.argv[1])
    
    words = ['hello', 'world']
    
    server = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port %s' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down')
        server.socket.close()
        
    print('Stopping server')
    server.socket.close()
    
    print('Done')
    
