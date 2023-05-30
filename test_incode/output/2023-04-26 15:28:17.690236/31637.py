#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'horse', 'sheep', 'cow', 'pig']
    for index, word in enumerate(words):
        print(index, word)
        if index == len(words) - 1:
            break
