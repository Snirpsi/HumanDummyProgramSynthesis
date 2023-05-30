#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and removes words. """    
    port = int(sys.argv[1])
    words = ['hello', 'world', 'how', 'are', 'you', '?']
    
    server = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port {}'.format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting')
        server.socket.close()
