#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and iterates over a list of words. """    
    port = int(sys.argv[1])
    words = []
    for x in range(1,port+1):
        words.append(str(x))
    
    server = HTTPServer(("", port), WordsHandler)
    server.serve_forever()
    
