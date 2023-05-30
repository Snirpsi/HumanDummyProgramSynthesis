#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers and enumerates words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    enumerated_words = []
    for number, word in enumerate(words):
        enumerated_words.append(word)
        enumerated_words.append('{}: {}'.format(number, word))
    print('\n'.join(enumerated_words))
    print('\n'.join(words))
    print('\n'.join(numbers))
    print('\n'.join(enumerated_words + words))
    print('\n'.join(numbers + words))
    print('\n'.join(numbers + numbers))
    print('\n'.join(numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + numbers + words))
    print('\n'.join(numbers + numbers + numbers + numbers + numbers + numbers + numbers + number