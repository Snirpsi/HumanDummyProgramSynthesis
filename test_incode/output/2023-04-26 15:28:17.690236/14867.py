#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(("", port), WordsServer)
    webserver.serve_forever()
    
