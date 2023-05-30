#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    words = ['cat', 'dog', 'mouse']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsHandler)
    
    server.serve_forever()
    
