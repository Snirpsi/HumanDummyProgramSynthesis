#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or stores numbers. """    
    words = []
    i = 0
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
            i += 1
    print('Number of words: {}'.format(len(words)))
    print('First 10 words: {}'.format(words[:10]))
    print('Last 10 words: {}'.format(words[-10:]))
    print('First 10 numbers: {}'.format(numbers[:10]))
    print('Last 10 numbers: {}'.format(numbers[-10:]))
    print('First 10 characters: {}'.format(characters[:10]))
    print('Last 10 characters: {}'.format(characters[-10:]))
    print('First 10 characters with spaces: {}'.format(characters[:10]))
    print('Last 10 characters with spaces: {}'.format(characters[-10:]))
    print('First 10 words with spaces: {}'.format(words[:10]))
    print('Last 10 words with spaces: {}'.format(words[-10:]))
    print('First 10 numbers with spaces: {}'.format(numbers[:10]))
    print('Last 10 numbers with spaces: {}'.format(numbers[-10:]))
    print('First 10 characters with spaces and punctuation: {}'.format(characters[:10]))
    print('Last 10 characters with spaces and punctuation: {}'.format(characters[-10:]))
    print('First 10 words with spaces and punctuation: {}'.format(words[:10]))
    print('Last 10 words with spaces and punctuation: {}'.format(words[-10:]))
    print('First 10 numbers with spaces and punctuation: {}'.format(numbers[:10]))
    print('Last 10 numbers with spaces and punctuation: {}'.format(numbers[-10:]))
    print('First 10 characters with spaces and punctuation and spaces: {}'.format(characters[:10]))
    print('Last 10 characters with spaces and punctuation and spaces: {}'.format(characters[-10:]))
    print('First 10 words with spaces and punctuation and spaces: {}'.format(words[:10]))
    print('Last 10 words with spaces and punctuation and spaces: {}'.format(words[-10:]))
    print('First 10 numbers with spaces and punctuation and spaces: {}'.format(numbers[:10]))
    print('Last 10 numbers with spaces and punctuation and spaces: {}'.format(numbers[-10:]))
    print('First 10 characters with spaces and punctuation and spaces and punctuation: {}'.format(characters[:10]))
    print('Last 10 characters with spaces and punctuation and spaces and punctuation: {}'.format(characters[-10:]))
    print('First 10 words with spaces and punctuation and spaces and punctuation: {}'.format(words[:10]))
    print('Last 10 words with spaces and punctuation and spaces and punctuation: {}'.format(words[-10:]))
    print('First 10 numbers with spaces and punctuation and spaces and punctuation: {}'.format(numbers[:10]))
    print('Last 10 numbers with spaces and punctuation and spaces and punctuation: {}'.format(numbers[-10:]))
    print('First 10 characters with spaces and punctuation and spaces and punctuation and 