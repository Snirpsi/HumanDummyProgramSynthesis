#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and converts numbers. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        try:
            number = int(word)
        except ValueError:
            print('Invalid input')
        else:
            words.append(word)
    
    numbers = []
    while True:
        number = input('Enter a number: ')
        if number == 'q':
            break
        try:
            number = int(number)
        except ValueError:
            print('Invalid input')
        else:
            numbers.append(number)
    
    words.sort()
    numbers.sort()
    
    print('The words are:')
    for word in words:
        print(word)
    print('The numbers are:')
    for number in numbers:
        print(number)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    