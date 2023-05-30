#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and removes words. """    
    
    port = '/dev/ttyUSB0'
    
    words = ['word1', 'word2', 'word3']
    
    words = remove_words(port, words)
    
    print(words)
    
