#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [port]" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    port = int(sys.argv[2])
    
    webserver = WebServer(filename, port)
    webserver.serve_forever()
    
