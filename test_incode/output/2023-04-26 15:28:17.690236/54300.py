#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or removes words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Serving at port", port)
    
    server.serve_forever()
