#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or stores numbers. """    
    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    numbers = []
    while True:
        number = input('Enter a number: ')
        if number == 'q':
            break
        numbers.append(number)
    
    numbers_converted = []
    for number in numbers:
        numbers_converted.append(int(number))
    
    words_converted = []
    for word in words:
        words_converted.append(word.lower())
    
    words_converted = list(set(words_converted))
    numbers_converted = list(set(numbers_converted))
    
    words_converted.sort()
    numbers_converted.sort()
    
    print('Words: ', words_converted)
    print('Numbers: ', numbers_converted)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
