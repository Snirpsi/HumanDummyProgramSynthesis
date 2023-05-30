#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and removes a list of numbers. """    
    words = []
    numbers = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
            number = int(input('Enter a number: '))
            numbers.append(number)
    
    words.sort()
    numbers.sort()
    
    print('\n'.join(words))
    print('\n'.join(numbers))
    
