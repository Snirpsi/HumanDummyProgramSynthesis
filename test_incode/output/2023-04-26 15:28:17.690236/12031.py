#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                words.append(line)
    
    words.sort()
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
