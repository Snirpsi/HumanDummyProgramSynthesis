#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or removes numbers. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip())
        if words:
            words = filter(lambda x: x != '', words)
        else:
            break
    print('\n'.join(words))
    
