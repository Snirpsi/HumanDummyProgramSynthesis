#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and opens a port. """    
    port = int(sys.argv[1])
    words = []
    
    server = HTTPServer(("", port), WordsHandler)
    