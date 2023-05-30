#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    words = []
    
    # Load words from file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Display all words
    print('\n'.join(words))
    
    # Start server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start server
    server.serve_forever()
    
