#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and stores a list of numbers. """    
    words = []
    numbers = []
    while True:
        word = input('Enter a word: ')
        if word == 'done':
            break
        numbers.append(int(input('Enter a number: ')))
        words.append(word)
    print('The words are:')
    for word in words:
        print(word)
    print('The numbers 