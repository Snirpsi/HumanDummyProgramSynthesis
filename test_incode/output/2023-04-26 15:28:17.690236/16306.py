#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or adds user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port ' + str(port) + '...')
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server...')
        server.socket.close()
        
    print('\nStopped.')
    
