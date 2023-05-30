#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words or prints all ports. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsHandler)
    server.serve_forever()
    
