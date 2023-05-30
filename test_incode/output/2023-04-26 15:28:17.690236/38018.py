#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or converts a port. """    
    
    port = sys.argv[1]
    
    server = HTTPServer(('', int(port)), WordsHandler)
    server.serve_forever()
