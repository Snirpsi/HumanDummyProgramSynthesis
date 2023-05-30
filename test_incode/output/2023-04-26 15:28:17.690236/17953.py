#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and prints numbers. """    
    
    words = ['cat', 'dog', 'mouse', 'rabbit', 'monkey']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
    
