#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split on whitespace
        words = line.split()
        
    # Print the list of words
    for word in words:
        print(word)
        
    # Print the total number of words
    print(len(words))
    
    # Run the server
    httpd = HTTPServer(('', 8000), WordsHandler)
    
    # Start the server
    httpd.serve_forever()
    
