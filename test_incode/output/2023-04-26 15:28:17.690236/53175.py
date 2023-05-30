#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words and returns a port. """    
    import sys
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        words.append(word)
    
    port = ''
    for word in words:
        port += word
        port += ' '
    
    print(port)
    
