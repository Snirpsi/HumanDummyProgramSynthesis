#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and enumerates all ports. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print('Server shut down.')
    
