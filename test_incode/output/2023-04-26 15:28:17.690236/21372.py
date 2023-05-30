#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or opens a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Starting server...")
    
    server.serve_forever()
    
    
