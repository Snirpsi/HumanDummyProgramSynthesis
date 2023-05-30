#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words[-1] == 'q':
            break
    print('The words are:')
    for word in words:
        print(word)
    print('The total is {}'.format(sum(words)))
    
