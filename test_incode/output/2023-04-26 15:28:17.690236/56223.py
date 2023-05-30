#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    server = BaseHTTPServer.HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
    
