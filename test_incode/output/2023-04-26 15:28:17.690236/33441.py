#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and multiplyes user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    
    server.serve_forever()
    
