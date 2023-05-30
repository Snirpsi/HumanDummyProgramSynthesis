#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and iterates over user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
