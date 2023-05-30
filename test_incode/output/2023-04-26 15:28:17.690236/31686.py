#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    port = 8080
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving at port {}'.format(port))
    
    server.serve_forever()
    
