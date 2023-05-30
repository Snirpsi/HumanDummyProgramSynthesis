#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    
    import sys
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), NumbersHandler)
    
    print('Serving at http://127.0.0.1:{}/'.format(port))
    
    server.serve_forever()
    
