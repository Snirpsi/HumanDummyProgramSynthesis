#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and multiplyes words. """    
    numbers = []
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input')
            continue
        else:
            break
    
    words = []
    while True:
        try:
            word = input('Enter a word: ')
            words.append(word)
        except ValueError:
            print('Invalid input')
            continue
        else:
            break
    
    numbers_multiplied = 0
    words_multiplied = 0
    
    for number in numbers:
        for word in words:
            numbers_multiplied += number * word
            words_multiplied += word
    
    print('The numbers are', numbers_multiplied, 'multiplied by', words_multiplied)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
