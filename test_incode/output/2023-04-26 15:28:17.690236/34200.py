#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or calculates a list of words. """    
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
    print('\nThe total words are:', len(words))
    print('\nThe average words are:', sum(words) / len(words))
    print('\nThe most common words are:')
    words = sorted(words, key=len)
    for word in words:
        print(word)
    print('\nThe least common words are:')
    words = sorted(words, key=lambda x: -len(x))
    for word in words:
        print(word)
    print('\nThe most common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe least common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe most common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe least common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe most common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe least common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe most common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe least common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe most common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe least common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe most common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe least common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe most common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe least common words are:')
    words = sorted(words, key=lambda x: -len(x), reverse=True)
    for word in words:
        print(word)
    print('\nThe most common words are:')
    words = sorted(words, key=lambda x: -