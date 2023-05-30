#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and returns numbers. """    
    
    words = ['cat', 'dog', 'pig']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Starting web server on port %d" % port)
    
    server.serve_forever()
    
