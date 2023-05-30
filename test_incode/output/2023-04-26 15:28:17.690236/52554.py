#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or returns a port. """    
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    
    server = HTTPServer(("", port), WordsHandler)
    server.serve_forever()
    
