#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split into words
        words = line.split(' ')
        
        # Store words in list
        words.extend(words)
    
    # Print words in list
    print(' '.join(words))
    
    # Start server
    httpd = HTTPServer(('', 80), WordsHandler)
    httpd.serve_forever()
    
