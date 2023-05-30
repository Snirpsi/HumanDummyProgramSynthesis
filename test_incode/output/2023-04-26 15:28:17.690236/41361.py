#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            break
        words.append(line)
        
    # Store words in global variable
    words = words
    
    # Start server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start server
    server.serve_forever()

<|/ file filename=wordlist.py source=github |>