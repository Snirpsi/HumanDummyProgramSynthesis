#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and prints a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Print each word
        print(' '.join(words))
        
    # Print final list
    print(' '.join(words))
    
    # Start server
    httpd = HTTPServer(('', PORT), WordsHandler)
    
    # Start server
    httpd.serve_forever()
    
