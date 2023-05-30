#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['word1', 'word2', 'word3']
    while True:
        words.extend(['word4', 'word5', 'word6'])
        print('words: ', words)
        time.sleep(5)
