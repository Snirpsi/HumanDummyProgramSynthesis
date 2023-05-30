#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or removes a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        server.server_close()
    
