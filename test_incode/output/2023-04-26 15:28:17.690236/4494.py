#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('The words are:')
    for word in words:
        print(word)
    print('')
    print('The total words is:', len(words))
    print('')
    print('The longest word is:', max(words))
    print('The shortest word is:', min(words))
    print('The average word length is:', sum(map(len, words)) / len(words))
    print('')
    print('The longest and shortest words are:')
    for word in words:
        if word == max(words):
            print('The word is', word, 'the longest word.')
        elif word == min(words):
            print('The word is', word, 'the shortest word.')
        else:
            print('The word is', word, 'the average word length.')
    print('')
    print('The longest and shortest words are:')
    for word in words:
        if word == max(words):
            print('The word is', word, 'the longest word.')
        elif word == min(words):
            print('The word is', word, 'the shortest word.')
        else:
            print('The word is', word, 'the average word length.')
    print('')
    print('The longest and shortest words are:')
    for word in words:
        if word == max(words):
            print('The word is', word, 'the longest word.')
        elif word == min(words):
            print('The word is', word, 'the shortest word.')
        else:
            print('The word is', word, 'the average word length.')
    print('')
    print('The longest and shortest words are:')
    for word in words:
        if word == max(words):
            print('The word is', word, 'the longest word.')
        elif word == min(words):
            print('The word is', word, 'the shortest word.')
        else:
            print('The word is', word, 'the average word length.')
    print('')
    print('The longest and shortest words are:')
    for word in words:
        if word == max(words):
            print('The word is', word, 'the longest word.')
        elif word == min(words):
            print('The word is', word, 'the shortest word.')
        else:
            print('The word is', word, 'the average word length.')
    print('')
    print('The longest and shortest words are:')
    for word in words:
        if word == max(words):
            print('The word is', word, 'the longest word.')
        elif word == min(words):
            print('The word is