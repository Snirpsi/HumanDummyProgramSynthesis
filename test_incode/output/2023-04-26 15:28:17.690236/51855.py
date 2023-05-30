#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    words = []
    
    # Read the words from the file 'words.txt'
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Print the words in the file 'words.txt'
    print('\n'.join(words))
    
    # Start the webserver
    webserver.run(host='0.0.0.0', port=8000)
    
