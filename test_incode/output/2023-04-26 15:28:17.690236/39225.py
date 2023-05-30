#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if len(line) == 0:
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Store words in list
        words.extend(words)
        
    # Store words in dictionary
    words = dict(zip(words, range(len(words))))
    
    # Print words in dictionary
    for word in words:
        print('%s: %d' % (word, words[word]))
    
    # Serve the web page
    httpd = HTTPServer(("", 8000), WordsHandler)
    httpd.serve_forever()

