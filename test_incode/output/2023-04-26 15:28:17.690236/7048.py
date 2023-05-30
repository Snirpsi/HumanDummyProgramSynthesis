#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    # Get the list of words from the file
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Start the server
    server = HTTPServer(("", 80), WordsHandler)
    
    # Start the server
    server.serve_forever()
    
