#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and removes a port. """    
    port = int(sys.argv[1])
    
    words = ['cat', 'dog', 'mouse']
    
    server = HTTPServer(('', port), WordsHandler)
    server.serve_forever()
