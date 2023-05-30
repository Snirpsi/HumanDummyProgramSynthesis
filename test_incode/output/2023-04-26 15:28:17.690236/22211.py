#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    port = int(sys.argv[1])
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    words.sort()
    
    sys.stdout.write('\n'.join(words))
    sys.stdout.write('\n')
    
    sys.stdout.flush()
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
