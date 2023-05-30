#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or enumerates a list of words. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    print('Numbers:')
    for number in numbers:
        print(number)
    
    print('Words:')
    for word in words:
        print(word)
    
    print('\n')
    
    print('Enumerate:')
    for index, word in enumerate(words):
        print('{:2}. {}'.format(index, word))
    
    print('\n')
    
    print('Enumerate with step:')
    for index, word in enumerate(words, 1):
        print('{:2}. {}'.format(index, word))
    
    print('\n')
    
    print('Enumerate with step and stepped index:')
    for index, word in enumerate(words, 1, 2):
        print('{:2}. {}'.format(index, word))
    
    print('\n')
    
    print('Enumerate with step and stepped index and stepped index:')
    for index, word in enumerate(words, 1, 3, 2):
        print('{:2}. {}'.format(index, word))
    
    print('\n')
    
    print('Enumerate with step and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and stepped index and step