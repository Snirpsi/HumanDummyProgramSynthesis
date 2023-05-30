#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and adds a list of words. """    
    
    words = []
    
    # Read the words from a file
    with open('words.txt', 'r') as f:
        words = [word.strip() for word in f.readlines()]
        
    # Print the words to stdout
    print('\n'.join(words))
    
    # Start the webserver
    webserver.run(host='0.0.0.0', port=8000)
    
    # 