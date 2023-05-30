#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words and multiplyes all ports. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    ports = [1,2,3,4,5]
    
    while True:
        for word in words:
            for port in ports:
                print('{} multiplied by {}'.format(word, port