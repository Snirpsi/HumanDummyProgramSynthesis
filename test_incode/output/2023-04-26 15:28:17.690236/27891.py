#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Remove leading and trailing whitespace
        line = line.lstrip()
        line = line.rstrip()
        
        # Remove any empty lines
        line = line.strip()
        
        # Append word to list
        words.append(line)
        
    # Print the list
    print(words)
    
    # Run the server
    httpd = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    httpd.serve_forever()

<|/ file source=github |>