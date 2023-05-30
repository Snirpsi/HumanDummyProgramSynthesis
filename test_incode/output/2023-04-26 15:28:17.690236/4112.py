#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and enumerates a list of numbers. """    
    
    port = sys.argv[1]
    
    server = None
    
    try:
        server = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    if server:
        server.socket.close()
    
    print('Done')
    
