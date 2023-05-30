#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    words = []
    
    # Read the words from the file 'words.txt'
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Print the words to the user
    print('\n'.join(words))
    
    # Start the webserver
    webserver.serve_forever()
    
