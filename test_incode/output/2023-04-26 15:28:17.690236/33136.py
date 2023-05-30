#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port {port}'.format(port=port))
    
    server.serve_forever()
    
