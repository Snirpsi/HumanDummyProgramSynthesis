#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'words.txt'
    
    words = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line != '':
                words.append(line)
    
    words.sort()
    
    server = BaseHTTPServer.HTTPServer(('localhost', 8000), WordsHandler)
    
    server.serve_forever()
