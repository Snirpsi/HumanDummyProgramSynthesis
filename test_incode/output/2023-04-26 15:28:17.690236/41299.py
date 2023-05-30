#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and stores a list of numbers. """    
    
    while True:
        word = input('Enter a word: ')
        numbers = []
        for letter in word:
            if letter.isdigit():
                numbers.append(int(letter))
            else:
                numbers.append(letter)
        
        print('The word "{}" has the following numbers: '.format(word))
        for number in numbers:
            print('