#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    words = []
    
    # Read the file into a list
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.rstrip())
    
    # Print the list
    print('\n'.join(words))
    
    # Start the server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start the server
    server.serve_forever()
