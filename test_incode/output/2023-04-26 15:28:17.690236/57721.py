#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or removes a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        server.serve_forever()
    else:
        ports = sys.argv[2:]
        for port in ports:
            port = int(port)
            server = HTTPServer(('', port), SimpleHTTPRequestHandler)
            server.serve_forever()
    
