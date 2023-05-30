#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words[-1] == 'q':
            break
    print('You entered', len(words), 'words')
    print('The first word was', words[0])
    print('The last word was', words[-1])
    print('The middle word was', words[len(words)//2])
    print('The middle word was', words[len(words)//2-1]