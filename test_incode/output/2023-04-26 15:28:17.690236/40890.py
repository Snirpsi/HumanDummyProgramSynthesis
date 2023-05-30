#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words == ['quit']:
            break
        print('The word is', *words)
        print('')
    print('Thank you!')
    
