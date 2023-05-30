#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = []
    
    # Open the word list file
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                words.append(line)
    
    # Open the word list in a browser
    browser = Browser()
    browser.open(words, 'words.txt')
    
    # Start the server
    