#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = []
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line or line[0] == '#':
                continue
            words.append(line)
    
    words.sort()
    
    port = 8000
    
    httpd = HTTPServer(('', port), WordsHandler)
    
    httpd.serve_forever()
    
