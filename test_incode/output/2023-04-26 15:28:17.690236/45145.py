#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words and multiplyes numbers. """    
    
    words = []
    numbers = []
    
    while True:
        word = input('Enter a word: ')
        numbers.append(int(input('Enter a number: ')))
        words.append(word)
        
        if word == 'q':
            break
        
    print('The words are:')
    for word in words:
        print(word)
    
    print('The numbers are:')
    for number in numbers:
        print(number)
    
    print('The product is:', numbers[0] * numbers[1])
    
