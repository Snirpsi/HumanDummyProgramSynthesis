#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
    
    # Calculate words with given frequencies
    words = [word for word in words if word in frequencies(words)]
    
    # Print the results
    for word in words:
        print(word)
    
    # Start a web server
    server = HTTPServer(("", port), WordsHandler)
    
    # Start a web server
    