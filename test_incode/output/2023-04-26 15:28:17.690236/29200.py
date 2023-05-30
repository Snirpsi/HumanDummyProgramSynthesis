#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and enumerates numbers. """    
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port}'.format(port=port))
    
    server.serve_forever()
    
