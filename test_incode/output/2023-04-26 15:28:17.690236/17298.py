#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port and multiplyes words. """    
    port = '/dev/ttyUSB0'
    words = ['word1', 'word2', 'word3']
    
    for word in words:
        words = word.split(' ')
        for word in words:
            print(word * 