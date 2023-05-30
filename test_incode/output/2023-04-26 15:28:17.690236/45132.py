#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and removes a list of words. """    
    
    # Load words from file
    words = []
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Remove words from file
    with open('words.txt', 'w') as f:
        for word in words:
            if word in open('words.txt').read():
                f.write('%s\n' % word)
    
    # Print list of words
    print('\n'.join(words))
    
    # Start webserver
    webserver.serve_forever()
    
