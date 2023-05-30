#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or removes a port. """    
    
    # Load words from a file
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Remove port
    words = [word for word in words if not word[:2] == 'http']
    
    # Print the list
    print('\n'.join(words))
    
    # Start webserver
    webserver = HTTPServer(('', 8080), Handler)
    webserver.serve_forever()
    
