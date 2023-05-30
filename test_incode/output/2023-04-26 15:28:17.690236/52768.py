#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words and multiplyes a list of numbers. """    
    words = []
    numbers = []
    
    while True:
        words.append(input('Enter a word: ').strip())
        numbers.append(int(input('Enter a number: ')))
        
        if len(words) == 3:
            break
        
    print('The product of ', numbers, ' is: ', words[0] * numbers[0])
    print('The product of ', numbers, ' is: ', words[1] * numbers[1])
    print('The product of ', numbers, ' is: ', words[2] * numbers[2])
    
