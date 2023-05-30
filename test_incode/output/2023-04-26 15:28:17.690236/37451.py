#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and iterates over a list of words. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer shutting down.')
        server.socket.close()
        
